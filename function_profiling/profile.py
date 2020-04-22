# -*- coding: utf-8 -*-

import cProfile
import pstats

import pandas as pd


def profile(func, **args):
    prof = cProfile.Profile()
    prof.enable()
    func(**args)
    prof.disable()
    stats = [key + value for key, value in pstats.Stats(prof).stats.items()]
    columns = [
        'file_name', 'line_number', 'function_name',
        'calls(all)', 'calls(only_external)', 'time(internal)', 'time(all)', 'callers']
    stats_df = pd.DataFrame(stats, columns=columns)
    return stats_df.sort_values(by=['file_name', 'line_number'])
