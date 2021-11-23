from das_dennis import DasDennis


if __name__ == "__main__":
    """Program to execute the Das-Dennis algorithm to generate weight files"""
    h = 12
    m = 3

    das_dennis_weight_generator = DasDennis(h, m)

    weight_vectors = das_dennis_weight_generator.get_weight_vectors()

    print("Number of vectors: " + str(len(weight_vectors)))
    print("Number of vectors: " + str(das_dennis_weight_generator.get_number_of_points()))
    for i in weight_vectors:
        print(i)

    das_dennis_weight_generator.save_to_file("W" + str(m) + "D_" + str(len(weight_vectors)) + ".dat", weight_vectors)
