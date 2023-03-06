#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Roya Babayev  
# DATE CREATED: 08/02/2023
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    
    Parameters:
    results_dic (dict): A dictionary with keys as image filenames and values as
        lists with the following elements:
        - idx 0: pet image label (string)
        - idx 1: classifier label (string)
        - idx 2: 1/0 (int) where 1 = match between pet image and classifier labels
                 and 0 = no match between labels
        - idx 3: 1/0 (int) where 1 = pet image 'is-a' dog and 0 = pet Image 
                 'is-NOT-a' dog.
        - idx 4: 1/0 (int) where 1 = Classifier classifies image 'as-a' dog and 
                 0 = Classifier classifies image 'as-NOT-a' dog.
    results_stats_dic (dict): A dictionary that contains the results statistics 
        (either a percentage or a count) where the key is the statistic's name 
        (starting with 'pct' for percentage or 'n' for count) and the value is 
        the statistic's value.
    model (str): Indicates which CNN model architecture will be used by the 
        classifier function to classify the pet images. Values must be one of:
        'resnet', 'alexnet', or 'vgg'.
    print_incorrect_dogs (bool): Whether to print incorrectly classified dog images.
    print_incorrect_breed (bool): Whether to print incorrectly classified dog breeds.
    
    Returns:
    None
    """
    
    # Print summary results
    print(f"Using the {model.upper()} CNN model architecture")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of \"Not-a\" Images: {results_stats_dic['n_notdogs_img']}")
    print(f"{results_stats_dic['pct_correct_dogs']}% Correct Dogs")
    print(f"{results_stats_dic['pct_correct_breed']}% Correct Breed")
    print(f"{results_stats_dic['pct_correct_notdogs']}% Correct \"Not-a\" Dog")
    print(f"{results_stats_dic['pct_match']}% Match")
    
    # Print incorrectly classified dogs
    if print_incorrect_dogs:
        print("\nMisclassified Dogs:")
        for image, values in results_dic.items():
            if sum(values[3:]) == 1:
                print(f"image: {image}, classifier label: {values[1]}")
    
    # Print incorrectly classified dog breeds
    if print_incorrect_breed:
        print("\nMisclassified Breeds of Dog:")
        for image, values in results_dic.items():
            if sum(values[3:]) == 2 and values[2] == 0:
                print(f"image: {image}, classifier label: {values[1]}")    
