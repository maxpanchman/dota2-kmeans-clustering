import math
import random
import intro

num_clusters = 4
clusters = []
centroids = []

def test():
    print('\nNUMBER OF CLUSTERS ', num_clusters)
    intro.load_data()       
    intro.normalize_data()     
    initialize_centroids()
    print_centroids()
    assign_clusters()
    create_clusters()
    print_clusters()
    update_centroids()
    print_centroids()

def generate_centroid():
    # Generate 9 random floats (from 0.0 to 1.0) for the 9 numerical features of Dota
    centroid = []
    for _ in range(9):
        centroid.append(random.uniform(0.0, 1.0))
    return centroid

def initialize_centroids():
    centroids.clear()
    i = 1
    while i <= num_clusters:
        centroids.append(generate_centroid())
        i = i + 1

def print_centroid(centroid):
    # Print the coordinates of the centroid (9 numbers)
    print(" ".join(['%6.3f' % feature for feature in centroid]))

def print_centroids():
    print('CENTROIDS')
    for centroid in centroids:
        print_centroid(centroid)

def euclidean_distance_sq(data_row, centroid):
    # Calculate distance ONLY for numerical columns (from index 2 to 10)
    # Index 0 (name) and 1 (primary attribute) are ignored
    total_sum = 0
    for i in range(2, 11):
        diff = centroid[i - 2] - data_row[i]
        total_sum += math.pow(diff, 2)
    return total_sum

def assign_clusters():
    for data_row in intro.krotkiNormal:
        minimum = 1e100
        minimum_index = 0
        for i in range(len(centroids)):
            next_dist = euclidean_distance_sq(data_row, centroids[i])
            if next_dist < minimum:
                minimum = next_dist
                minimum_index = i
        # Save the found cluster number at the end (index 11)
        data_row[11] = minimum_index

def create_clusters():
    clusters.clear()
    for i in range(0, len(centroids)):
        cluster = []
        for data_row in intro.krotkiNormal:
            if data_row[11] == i:
                cluster.append(data_row)
        clusters.append(cluster)

def print_cluster(cluster_num):
    print('\nCLUSTER NUMBER ', cluster_num, ' (Number of heroes:', len(clusters[cluster_num]), ')')
    for data_row in clusters[cluster_num]:
        # Print name [0], attribute [1], and cluster number [11]
        print('%-25s %-5s Cluster: %d' % (data_row[0], data_row[1], data_row[11]))

def print_clusters():
    for number in range(0, len(centroids)):
        print_cluster(number)

def calculate_new_centroid(cluster):
    if len(cluster) == 0:
        return generate_centroid()
    
    # Create an array of 9 zeros to sum each feature
    sums = [0.0] * 9
    for data_row in cluster:
        for i in range(2, 11):
            sums[i - 2] += data_row[i]
            
    # Divide the sum by the number of heroes in the cluster (finding the new mean)
    new_centroid = []
    for s in sums:
        new_centroid.append(s / len(cluster))
    return new_centroid

def update_centroids():
    centroids.clear()
    print('\nShifted centroids ------------')
    for nr in range(num_clusters):
        centroids.append(calculate_new_centroid(clusters[nr]))
