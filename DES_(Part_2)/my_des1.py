import simpy
import random
import pandas as pd


class g:
	patient_inter = 5
	mean_n_consult_time = 6
	number_of_nurses = 1
	sim_duration = 120
	number_of_runs = 5

class Patient:
	def __init__(self, p_id):
		self.id = p_id
		self.q_time_nurse = 0

class Model:
	def __init__(self, run_number):
		self.env = simpy.Environment()
		self.patient_counter = 0
		self.nurse = simpy.Resource(self.env, capacity=g.number_of_nurses)
		self.run_number = run_number
		self.results_df = pd.DataFrame()
		self.results_df["Patient ID"] = [1]
		self.results_df["Q Time Nurse"] = [0.0]
		self.results_df["Time with Nurse"] = [0.0]
		self.results_df.set_index("Patient ID", inplace=True)
		self.mean_q_time_nurse = 0

	def generator_patient_arrivals(self):
		while True:
			self.patient_counter += 1
			p = Patient(self.patient_counter)
			self.env.process(self.attend_clinic(p))
			sampled_inter = random.expovariate(1.0 / g.patient_inter)
			yield self.env.timeout(sampled_inter)

	def attend_clinic(self, patient):
		start_q_nurse = self.env.now
		with self.nurse.request() as req:
			yield req
			end_q_nurse = self.env.now
			patient.a_time_nurse = end_q_nurse - start_q_nurse
			sampled_nurse_act_time = random.expovariate(1.0 / g.mean_n_cousult_time)
		self.results_df.at[patient.id, "Q Time Nurse"] = (patient.q_time_nurse)
		self.results_df.at[patient.id, "Time with Nurse"] = (sampled_nurse_act_time)
		yield self.env.timeout(sampled_nurse_act_time)

	def calculate_run_results(self):
		self.mean_q_time_nurse = self.results_df["Q Time Nurse"].mean()

	def run(self):
		self.env.process(self.generator_patient_arrivals())
		self.env.run(until=g.sim_duration)
		self.calculate_sun_results()
		print(f"Sum Number {self.run_number}")
		print(self.results_df)

class Trial:
	def __init__(self):
		self.df_trial_results = pd.DataFrame()
		self.df_trial_results["Runn Number"] = [0]
		self.df_trial_results["Mean Q Time Nurse"] = [0.0]
		self.df_trial_results.set_index("Run Number", inplace=True)
	def print_trial_results(self):
		print("Trial Results")
		print(self.df_trial_results)
	def run_trial(self):
		for run in range(g.number_of_runs):
			my_model = Model(run)
			my_model.run()
			self.df__trial_results.loc[run] = [my_model.mean_q_time_nurse]
		self.print_trial_results()

my_trial = Trial()

my_trial.run_trial()
