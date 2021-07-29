import path_resolver
from src.analysis.cluster import movielens, cluster, analysis, post_process
from src.analysis.simulate import simulate

# FOR All_Neutral
run = simulate('ease', 'All_Neutral')
run_output = run.run_dynamics(n_i=10, n_u=0, n_r=30, steps=5, n_clusters = 2)

# save the plot_counts() and plot_percent pngs
analyse = analysis(run_output[1])
analyse.rename_cluster(1,1000)
analyse.plot_counts(show=False, loc=run.run_name+'/counts.png')
analyse.plot_percent(show=False, loc=run.run_name+'/percent.png')