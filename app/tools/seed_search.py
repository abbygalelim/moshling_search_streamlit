from tools.constants import MOSHLINGS_SEED_COMBOS, SEED_FILE_DICT


def search_moshling_by_seed(
    selected_combo: list, type_of_results: str = 'General', all_seed_combos: dict[str, list] = MOSHLINGS_SEED_COMBOS
):
    '''
    Param: a list representing the colors and types of each seed and a str representing either specific or general
    Return: list of names of moshling whose combinations include the specified seeds
    '''
    selected_combo.sort(key=lambda x: x[0], reverse=True)

    ret = []

    for mosh, curr_combo in all_seed_combos.items():
        match = True
        curr_combo_copy = curr_combo.copy()

        if 'mission' in curr_combo:
            match = False

        if match:
            for plant in selected_combo:
                colored = plant not in SEED_FILE_DICT
                any_plant = '_'.join(plant.split('_')[:-1]) if colored else plant

                if type_of_results == 'Specific':
                    if plant in curr_combo_copy:
                        curr_combo_copy.remove(plant)
                    else:
                        match = False
                        break
                else:
                    if plant not in SEED_FILE_DICT:  # Color is specified
                        if plant in curr_combo_copy:  # First, try to find exact match
                            curr_combo_copy.remove(plant)
                        else:  # Else, try to find general match
                            if any_plant in curr_combo_copy:
                                curr_combo_copy.remove(any_plant)
                            else:
                                match = False
                                break
                    else:  # Color is not specified
                        if plant in curr_combo_copy:
                            curr_combo_copy.remove(plant)
                        else:
                            pop_i = -1
                            for i in range(len(curr_combo_copy)):
                                if plant in curr_combo_copy[i]:
                                    pop_i = i
                                    break
                            if pop_i != -1:
                                curr_combo_copy.pop(i)
                            else:
                                match = False
                                break
        if match:
            ret.append(mosh)

    return ret
