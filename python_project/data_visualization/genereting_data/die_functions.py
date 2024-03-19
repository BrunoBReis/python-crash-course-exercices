from die import Die
import plotly.express as px
import numpy as np


def roll_dices(dices: list, times: int):
    """Rolls dices for x times, creating a list in a list"""
    results = []
    for rull_num in range(times):
        dice_roll = [dice.roll() for dice in dices]
        results.append(dice_roll)
    return results


def sum_dices(results: list):
    """Sum each pair of dice"""
    sum_dices = []
    for roll_dice in results:
        each_list = sum(roll_dice)
        sum_dices.append(each_list)
    return sum_dices


def multiply_dices(results: list):
    """Multiply each pair of dice"""
    mult_dices = []
    for roll_dice in results:
        each_list = np.prod(roll_dice)
        mult_dices.append(each_list)
    return mult_dices


# Can't be use because poss_result is not adapted
def max_value(dices: list[Die]):
    """Calculates the max value for dices"""
    count = 0
    for dice in dices:
        count += dice.num_sides
    return count


def poss_result_die(dices: list[Die]):
    """Create a range for your dices"""
    max_dice_value = max_value(dices)
    min_dice_value = len(dices)
    return range(min_dice_value, max_dice_value + 1) # Have to change


def frequency(dices: list[Die], results: list):
    """Claculates frenquency of results in dices"""
    frequencies = []
    poss_result = poss_result_die(dices)
    for result in list(poss_result):
        freq = results.count(result)
        frequencies.append(freq)
    return frequencies
