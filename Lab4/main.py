import time

from exact_weight import ExactWeightSampling
from extended_olken import ExtendedSampling
from online_exploration import OnlineExplorationSampling
from draw import draw_time_cost


def do_exact_weight_sampling(sample_nums, db_file, popular_user_file, twitter_user_file):
    print("Exact Weight Sampling")
    ew_sampling = ExactWeightSampling(db_file, popular_user_file, twitter_user_file)
    relations = ["Popular_user", "Twitter_user", "Twitter_user"]
    start_time = time.process_time()
    ew_sampling.exact_weight(relations)
    end_time = time.process_time()
    build_weight_cost = end_time - start_time
    print("Build Weight Cost: ", build_weight_cost)
    time_costs = []
    for sample_num in sample_nums:
        print("Sample Num: ", sample_num)
        time_cost = ew_sampling.sample(sample_num, relations)
        time_costs.append(time_cost)
    for i in range(len(time_costs)):
        time_costs[i] += build_weight_cost
    return time_costs


def do_extended_olken_sampling(sample_nums, db_file, popular_freq_file, twitter_freq_file):
    print("Extended Olken Sampling")
    eo_sampling = ExtendedSampling(db_file, popular_freq_file, twitter_freq_file)
    relations = ["Popular_user", "Twitter_user", "Twitter_user"]
    start_time = time.process_time()
    eo_sampling.extended_olken(600, popular_freq_file, twitter_freq_file, relations)
    end_time = time.process_time()
    build_weight_cost = end_time - start_time
    print("Build Weight Cost: ", build_weight_cost)
    h = 600
    time_costs = []
    for sample_num in sample_nums:
        print("Sample Num: ", sample_num)
        time_cost = eo_sampling.sample(sample_num, relations, h, popular_freq_file, twitter_freq_file)
        time_costs.append(time_cost)
    for i in range(len(time_costs)):
        time_costs[i] += build_weight_cost
    return time_costs


def do_online_exploration_sampling(sample_nums, db_file, popular_freq_file, twitter_freq_file):
    print("Online Exploration Sampling")
    oe_sampling = OnlineExplorationSampling(db_file, popular_freq_file, twitter_freq_file)
    threshold = 50
    relations = ["Popular_user", "Twitter_user", "Twitter_user"]
    random_walk_time = 200
    alpha = 0.9
    start_time = time.process_time()
    oe_sampling.online_exploration(threshold, relations, random_walk_time, alpha)
    end_time = time.process_time()
    build_weight_cost = end_time - start_time
    print("Build Weight Cost: ", build_weight_cost)
    time_costs = []
    for sample_num in sample_nums:
        print("Sample Num: ", sample_num)
        time_cost = oe_sampling.sample(sample_num, relations, threshold, random_walk_time, alpha)
        time_costs.append(time_cost)
    for i in range(len(time_costs)):
        time_costs[i] += build_weight_cost
    return time_costs

def main():
    db_file = "data/twitter_combined.db"
    popular_freq_file = "data/popular_frequency.txt"
    twitter_freq_file = "data/twitter_frequency.txt"
    sample_nums = range(10, 151, 10)
    ew_time_costs = do_exact_weight_sampling(sample_nums, db_file, popular_freq_file, twitter_freq_file)
    eo_time_costs = do_extended_olken_sampling(sample_nums, db_file, popular_freq_file, twitter_freq_file)
    oe_time_costs = do_online_exploration_sampling(sample_nums, db_file, popular_freq_file, twitter_freq_file)
    ew_time = []
    eo_time = []
    oe_time = []
    for sample_num, ew_time_cost in zip(sample_nums, ew_time_costs):
        ew_time.append((sample_num, ew_time_cost))
    for sample_num, eo_time_cost in zip(sample_nums, eo_time_costs):
        eo_time.append((sample_num, eo_time_cost))
    for sample_num, oe_time_cost in zip(sample_nums, oe_time_costs):
        oe_time.append((sample_num, oe_time_cost))
    draw_time_cost(ew_time, eo_time, oe_time)


if __name__ == "__main__":
    main()
