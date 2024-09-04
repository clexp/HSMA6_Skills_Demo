import simpy
import random
import pandas as pd


class g:
    plane_inter = 3
    mean_tower_time = 6
    mean_gate_time = 135
    mean_exit_time = 17
    number_of_tower_handlers = 1
    number_of_gates = 30
    number_of_exit_slots = 2
    sim_duration = 24 * 60
    number_of_runs = 100


class Plane:
    def __init__(self, p_id):
        self.id = p_id
        self.q_time_tower = 0
        self.q_time_gate = 0
        self.q_time_slots = 0


class Model:
    def __init__(self, run_number):
        self.env = simpy.Environment()
        self.plane_counter = 0
        self.tower = simpy.Resource(self.env, capacity=g.number_of_tower_handlers)
        self.gate = simpy.Resource(self.env, capacity=g.number_of_gates)
        self.exit = simpy.Resource(self.env, capacity=g.number_of_exit_slots)
        self.run_number = run_number
        self.results_df = pd.DataFrame()
        self.results_df["Plane ID"] = [1]
        self.results_df["Q Time Tower"] = [0.0]
        self.results_df["Time with Tower"] = [0.0]
        self.results_df["Q Time Gate"] = [0.0]
        self.results_df["Time at Gate"] = [0.0]
        self.results_df["Q Time exit"] = [0.0]
        self.results_df["Time at exit"] = [0.0]
        self.results_df.set_index("Plane ID", inplace=True)
        self.mean_q_time_doctor = 0
        self.mean_q_time_recep = 0
        self.mean_q_time_nurse = 0

    def generator_plane_arrivals(self):
        while True:
            self.plane_counter += 1
            p = Plane(self.plane_counter)
            self.env.process(self.visit_LHR(p))
            sampled_inter = random.expovariate(1.0 / g.plane_inter)
            yield self.env.timeout(sampled_inter)

    def visit_LHR(self, plane):
        start_q_tower = self.env.now
        with self.tower.request() as req:
            yield req
            end_q_tower = self.env.now
            plane.q_time_tower = end_q_tower - start_q_tower
            sampled_tower_act_time = random.expovariate(1.0 / g.mean_tower_time)
            self.results_df.at[plane.id, "Q Time Tower"] = plane.q_time_tower
            self.results_df.at[plane.id, "Time with Tower"] = sampled_tower_act_time
            yield self.env.timeout(sampled_tower_act_time)
        start_q_gate = self.env.now
        with self.gate.request() as req:
            yield req
            end_q_gate = self.env.now
            plane.q_time_gate = end_q_gate - start_q_gate
            sampled_gate_act_time = random.expovariate(1.0 / g.mean_gate_time)
            self.results_df.at[plane.id, "Q Time Gate"] = plane.q_time_gate
            self.results_df.at[plane.id, "Time at Gate"] = sampled_gate_act_time
            yield self.env.timeout(sampled_gate_act_time)
        start_q_exit = self.env.now
        with self.exit.request() as req:
            yield req
            end_q_exit = self.env.now
            plane.q_time_exit = end_q_exit - start_q_exit
            sampled_exit_act_time = random.expovariate(
                1.0 / g.mean_exit_time
            )
            self.results_df.at[plane.id, "Q Time Exit"] = plane.q_time_exit
            self.results_df.at[plane.id, "Time at exit"] = (
                sampled_exit_act_time
            )
            yield self.env.timeout(sampled_exit_act_time)

    def calculate_run_results(self):
        self.mean_q_time_tower = self.results_df["Q Time Tower"].mean()
        self.mean_q_time_gate = self.results_df["Q Time Gate"].mean()
        self.mean_q_time_exit = self.results_df["Q Time Exit"].mean()

    def run(self):
        self.env.process(self.generator_plane_arrivals())
        self.env.run(until=g.sim_duration)
        self.calculate_run_results()
        print(f"Rum Number {self.run_number}")
        print(self.results_df)


class Trial:
    def __init__(self):
        self.df_trial_results = pd.DataFrame()
        self.df_trial_results["Run Number"] = [0]
        self.df_trial_results["Mean Q Time Tower"] = [0.0]
        self.df_trial_results["Mean Q Time Gate"] = [0.0]
        self.df_trial_results["Mean Q Time Exit"] = [0.0]
        self.df_trial_results.set_index("Run Number", inplace=True)

    def print_trial_results(self):
        print("Trial Results")
        print(self.df_trial_results)

    def run_trial(self):
        for run in range(g.number_of_runs):
            my_model = Model(run)
            my_model.run()
            self.df_trial_results.loc[run] = [
                my_model.mean_q_time_tower,
                my_model.mean_q_time_gate,
                my_model.mean_q_time_exit,
            ]
        self.print_trial_results()


my_trial = Trial()

my_trial.run_trial()
