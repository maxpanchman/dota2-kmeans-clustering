import intro
import calcul

# Limit the number of loop iterations
max_iterations = 20

def main():
    print('\nNUMBER OF CLUSTERS ', calcul.num_clusters)
    
    intro.load_data()
    intro.normalize_data()

    calcul.initialize_centroids()
    calcul.print_centroids()
    calcul.assign_clusters()
    calcul.create_clusters()
    calcul.print_clusters()

    # The main execution loop with an iteration limit
    repeat = 0
    while repeat < max_iterations:
        calcul.update_centroids()
        calcul.print_centroids()
        calcul.assign_clusters()
        calcul.create_clusters()
        calcul.print_clusters()
        repeat += 1

# Run the main function of the program
if __name__ == "__main__":
    main()
