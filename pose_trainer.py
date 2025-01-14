import argparse
import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt

from parse import parse_sequence, load_ps
from evaluate import evaluate_pose

def evaluate_npy(file_path, exercise) :
    if file_path:
        print(file_path)

        pose_seq = load_ps(file_path)

        (correct, feedback) = evaluate_pose(pose_seq, exercise)
        print(correct)
        if correct:
            print('Exercise performed correctly!')
        else:
            print('Exercise could be improved:')
            print(feedback)
    else:
        print('No npy file specified.')
        return
