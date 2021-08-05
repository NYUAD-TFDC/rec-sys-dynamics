import path_resolver
import argparse
from src.analysis.cluster import movielens, cluster, analysis, post_process
from src.analysis.simulate import simulate

parser = argparse.ArgumentParser(
    description="Example script to replicate results obtained on user dynamics in recommender systems"
)

parser.add_argument('algo', help= "Name of algorithm: 'ease', 'cosin', or 'mf'")
parser.add_argument('dataset', help= "Name of dataset: \
                            'All_Neutral',\
                            '1_Biased_Communities_Control', \
                            '2_Biased_Communities_Control', \
                            'Biased_Neutral_Control'") 

args = parser.parse_args()

# FOR All_Neutral
run = simulate(str(args.algo), str(args.dataset))
run_output = run.run_dynamics(n_i=10, n_u=0, n_r=30, steps=5, n_clusters = 2)

# save the plot_counts() and plot_percent pngs
analyse = analysis(run_output[1])
analyse.rename_cluster(1,1000)
analyse.plot_counts(show=False, loc=run.run_name+'/counts.png')
analyse.plot_percent(show=False, loc=run.run_name+'/percent.png')