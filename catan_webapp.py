import streamlit as st
from more_itertools import flatten
import matplotlib.pyplot as plt
import networkx as nx
import random

def desert_node_finder(board_dict):
    output = ''
    for key,value in board_dict.items():
        if value['element'] == 'desert':
            output = key
    return output

def apply_catan_structure_to_graph(T):
    layout = nx.spring_layout(T)
    layout['A'] = [-1, 2]
    layout['B'] = [0, 2]
    layout['C'] = [1, 2]

    layout['D'] = [-1.5, 1]
    layout['E'] = [-0.5, 1]
    layout['F'] = [0.5, 1]
    layout['G'] = [1.5, 1]

    layout['H'] = [-2, 0]
    layout['I'] = [-1, 0]
    layout['J'] = [0, 0]
    layout['K'] = [1, 0]
    layout['L'] = [2, 0]

    layout['M'] = [-1.5, -1]
    layout['N'] = [-0.5, -1]
    layout['O'] = [0.5, -1]
    layout['P'] = [1.5, -1]

    layout['Q'] = [-1, -2]
    layout['R'] = [0, -2]
    layout['S'] = [1, -2]

    return layout

def list_of_lists_to_single_list(list_of_lists):
    output_list = []
    for i in range(len(list_of_lists)):
        output_list += list_of_lists[i]
    return output_list

def ultimate_board_dict(empty_board_dict):
    output_dict = {}
    for key,value in empty_board_dict.items():
        if key not in output_dict:
            output_dict[key] = {'neighbors':[x for x in list(flatten(value)) if x != key],'element':'','element_rule':False, 'number':'', 'number_rule':False}
    return output_dict

def element_pool(lumber, brick, wool, grain, ore, desert):
    output = []
    output += ['lumber' for _ in range(lumber)]
    output += ['brick' for _ in range(brick)]
    output += ['wool' for _ in range(wool)]
    output += ['grain' for _ in range(grain)]
    output += ['ore' for _ in range(ore)]
    output += ['desert' for _ in range(desert)]
    random.shuffle(output)
    return output

def number_pool(two, three, four, five, six, eight, nine, ten, eleven, twelve):
    output_blackspot,  output_hotspot= [], []
    output_blackspot += [2 for _ in range(two)]
    output_blackspot += [3 for _ in range(three)]
    output_blackspot += [4 for _ in range(four)]
    output_blackspot += [5 for _ in range(five)]

    output_hotspot += [6 for _ in range(six)]
    output_hotspot += [8 for _ in range(eight)]

    output_blackspot += [9 for _ in range(nine)]
    output_blackspot += [10 for _ in range(ten)]
    output_blackspot += [11 for _ in range(eleven)]
    output_blackspot += [12 for _ in range(twelve)]

    random.shuffle(output_blackspot)
    random.shuffle(output_hotspot)
    return output_blackspot, output_hotspot

def remove_all_ocurrences(input_list, removed_element):
    output_list = []
    for x in input_list:
        if x != removed_element:
            output_list.append(x)
    return output_list

def dictionary_of_colors(ultimate_beard_dict):
    output_dict = {}
    for key,value in ultimate_beard_dict.items():
        if value['element'] == 'lumber':
            output_dict[key] = 'green'
        elif value['element'] == 'brick':
            output_dict[key] = 'firebrick'
        elif value['element'] == 'wool':
            output_dict[key] = 'lawngreen'
        elif value['element'] == 'grain':
            output_dict[key] = 'gold'
        elif value['element'] == 'ore':
            output_dict[key] = 'mediumorchid'
        elif value['element'] == 'desert':
            output_dict[key] = 'wheat'
        else:
            output_dict[key] = 'black'
    return output_dict

def dictionary_of_numbers(ultimate_beard_dict):
    output_dict = {}
    for key,value in ultimate_beard_dict.items():
        output_dict[key] = str(value['number'])
    return output_dict

st.markdown('# Random for Catan Board Generator')
st.write('by Luis Antonio Garcia')
st.write('')
st.write('')
desert_center = st.checkbox('Desert in the middle?')
run_button = st.button('Generate a new random Catan Board!', type = 'primary')

if run_button:
    empty_board_dict = {
    'A':[('A','B'), ('A','D'), ('A','E')], 
    'B':[('B','A'), ('B','C'), ('B','E'), ('B','F')],
    'C':[('C','B'), ('C','F'), ('C','G')],

    'D':[('D','A'), ('D','E'), ('D','H'), ('D','I')],
    'E':[('E','A'), ('E','B'), ('E','D'), ('E','F'), ('E','I'), ('E','J')],
    'F':[('F','B'), ('F','C'), ('F','E'), ('F','G'), ('F','J'), ('F','K')],
    'G':[('G','C'), ('G','F'), ('G','K'), ('G','L')],

    'H':[('H','D'), ('H','I'), ('H','M')],
    'I':[('I','D'), ('I','E'), ('I','H'), ('I','J'), ('I','M'), ('I','N')],
    'J':[('J','E'), ('J','F'), ('J','I'), ('J','K'), ('J','N'), ('J','O')],
    'K':[('K','F'), ('K','G'), ('K','J'), ('K','L'), ('K','O'), ('K','P')],
    'L':[('L','G'), ('L','K'), ('L','P')],

    'M':[('M','H'), ('M','I'), ('M','N'), ('M','Q')],
    'N':[('N','I'), ('N','J'), ('N','M'), ('N','O'), ('N','Q'), ('N','R')],
    'O':[('O','J'), ('O','K'), ('O','N'), ('O','P'), ('O','R'), ('O','S')],
    'P':[('P','K'), ('P','L'), ('P','O'), ('P','S')],

    'Q':[('Q','M'), ('Q','N'), ('Q','R')],
    'R':[('R','N'), ('R','O'), ('R','Q'), ('R','S')],
    'S':[('S','O'), ('S','P'), ('S','R')]
    }

    #Element routine
    board_dict = ultimate_board_dict(empty_board_dict)
    if desert_center:
        element_pool_list = element_pool(lumber=4, brick=3, wool=4, grain=4, ore=3, desert=0)
        node_name_list = [*empty_board_dict.keys()]
        node_name_list = remove_all_ocurrences(node_name_list, 'J')
        board_dict['J']['element'] = 'desert'
    else:
        element_pool_list = element_pool(lumber=4, brick=3, wool=4, grain=4, ore=3, desert=1)
        node_name_list = [*empty_board_dict.keys()]

    while len(node_name_list) > 0:
        random_node = random.choice(node_name_list)
        random_element = random.choice(element_pool_list)
        neighbor_elements = [y for y in [board_dict[x]['element'] for x in board_dict[random_node]['neighbors']] if y]
        if random_element in neighbor_elements:
            second_trial_counter = 1
            for i in range(len(element_pool_list)):
                if second_trial_counter != len(element_pool_list):
                    if element_pool_list[i] not in neighbor_elements:
                        board_dict[random_node]['element'] = element_pool_list[i]
                        board_dict[random_node]['element_rule'] = True
                        node_name_list = remove_all_ocurrences(node_name_list, random_node)
                        element_pool_list.remove(element_pool_list[i])
                        break
                    else:
                        second_trial_counter += 1
                else:
                    board_dict[random_node]['element'] = random_element
                    node_name_list = remove_all_ocurrences(node_name_list, random_node)
                    element_pool_list.remove(random_element)
        else:
            board_dict[random_node]['element'] = random_element
            board_dict[random_node]['element_rule'] = True
            node_name_list = remove_all_ocurrences(node_name_list, random_node)
            element_pool_list.remove(random_element)
    node_colors = dictionary_of_colors(board_dict)

    #Number routine
    number_pool_blackspot, number_pool_hotspot = number_pool(two=1, three=2, four=2, five=2, six=2, eight=2, nine=2, ten=2, eleven=2, twelve=1)
    node_name_list = [*empty_board_dict.keys()]
    desert_node = desert_node_finder(board_dict)
    node_name_list = remove_all_ocurrences(node_name_list, desert_node)

    while len(number_pool_hotspot) > 0:
        random_node = random.choice(node_name_list)
        while random_node == desert_node:
            random_node = random.choice(node_name_list)
        random_number = random.choice(number_pool_hotspot)
        neighbor_numbers = [y for y in [board_dict[x]['number'] for x in board_dict[random_node]['neighbors']] if y]
        if neighbor_numbers != []:
            while neighbor_numbers != []:
                random_node = random.choice(node_name_list)
                neighbor_numbers = [y for y in [board_dict[x]['number'] for x in board_dict[random_node]['neighbors']] if y]
            board_dict[random_node]['number'] = random_number
            board_dict[random_node]['number_rule'] = True
            node_name_list = remove_all_ocurrences(node_name_list, random_node)
            number_pool_hotspot.remove(random_number)
        else:
            board_dict[random_node]['number'] = random_number
            board_dict[random_node]['number_rule'] = True
            node_name_list = remove_all_ocurrences(node_name_list, random_node)
            number_pool_hotspot.remove(random_number)

    while len(number_pool_blackspot) > 0:
        random_node = random.choice(node_name_list)
        random_number = random.choice(number_pool_blackspot)
        if random_number in [6,8]:
            neighbor_numbers = [y for y in [board_dict[x]['number'] for x in board_dict[random_node]['neighbors']]+[6,8] if y]
        else:
            neighbor_numbers = [y for y in [board_dict[x]['number'] for x in board_dict[random_node]['neighbors']] if y]
        if board_dict[random_node]['element'] == 'desert':
            board_dict[random_node]['number_rule'] = True
            node_name_list = remove_all_ocurrences(node_name_list, random_node)
        else:
            if random_number in neighbor_numbers:
                second_trial_counter = 1
                for i in range(len(number_pool_blackspot)):
                    if second_trial_counter != len(number_pool_blackspot):
                        if number_pool_blackspot[i] not in neighbor_numbers:
                            board_dict[random_node]['number'] = number_pool_blackspot[i]
                            board_dict[random_node]['number_rule'] = True
                            node_name_list = remove_all_ocurrences(node_name_list, random_node)
                            number_pool_blackspot.remove(number_pool_blackspot[i])
                            break
                        else:
                            second_trial_counter += 1
                    else:
                        board_dict[random_node]['number'] = random_number
                        node_name_list = remove_all_ocurrences(node_name_list, random_node)
                        number_pool_blackspot.remove(random_number)
            else:
                board_dict[random_node]['number'] = random_number
                board_dict[random_node]['number_rule'] = True
                node_name_list = remove_all_ocurrences(node_name_list, random_node)
                number_pool_blackspot.remove(random_number)
    node_numbers = dictionary_of_numbers(board_dict)

    #Graph visualization
    T = nx.Graph()
    T.add_nodes_from(empty_board_dict.keys())
    T.add_edges_from(list_of_lists_to_single_list([*empty_board_dict.values()]))

    fig, ax = plt.subplots()
    nx.draw_networkx(T, labels = node_numbers, pos=apply_catan_structure_to_graph(T), node_color=[node_colors[node] if node in node_colors else 'black' for node in T.nodes()])
    st.pyplot(fig)
