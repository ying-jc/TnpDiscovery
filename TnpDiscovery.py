#!/usr/bin/env python

import classif_pred
import click

@click.command()
@click.option('--conf', nargs=1, required=False, type=str, prompt='Config file name', help='Configuration file in plain text format. (Required)')
@click.option('--seq', nargs=1, required=False, type=str, prompt='Sequence file name', help='Protein sequence file in fasta format. (Required)')
@click.option("--classif", nargs=1, required=False, default='EC-all',type=click.Choice(['EC-all', 'GBM-best'], case_sensitive=True), help="Choose a classifier. [Default: EC-all] (Optional)")
@click.option("--cutoff", nargs=1, required=False, default=0.606,type=click.FloatRange(0,1), help="Cutoff value for binary classification. [Default: 0.606] (Optional)")
@click.option('--n_proc',nargs=1, required=False, default=1, type=click.IntRange(1,None), help='Number of processes used for feature extraction. [Default: 1] (Optional)')
@click.option('--terminal', nargs=1, required=False, default='True', type=click.Choice(['True', 'False'], case_sensitive=True), help='Output result to the terminal. [Default: True] (Optional)')
@click.option('--out', nargs=1, required=False, default=None, type=str, help='The name of the output file in tab-delimited text format. (Optional)')

def run_command(n_proc,seq,conf,classif,cutoff,terminal,out):
    """TnpDiscovery: A machine learning-based tool for the discovery of prokaryotic transposases from protein features"""
    classif_pred.mod_predict(n_proc,seq,conf,classif,cutoff,terminal,out)
    print('\nWork done!')

if __name__ == '__main__':
    run_command()
    