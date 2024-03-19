from die import Die
import plotly.express as px
from die_functions import roll_dices, frequency, sum_dices, poss_result_die, multiply_dices


def main():

    # Create a D6 and D10
    die_1 = Die()
    die_2 = Die()
    die_3 = Die()
    dices = [die_1, die_2, die_3]

    # Make some rolls
    current_dices = roll_dices(dices, 10_000)
    print(current_dices)

    # Summing then
    summing = sum_dices(current_dices)
    print(summing)

    # Analyze results
    freq = frequency(dices, summing)
    print(freq)

    # Poss result
    poss_result = poss_result_die(dices)

    # Visualize results
    title = "Results of rolling a D6 and D10 50000 times"
    labels = {'x': 'Result',
              'y': 'Frequency of Result'}
    fig = px.bar(x=poss_result, y=freq, title=title, labels=labels)
    # Customization
    fig.update_layout(xaxis_dtick=1) # Every label is visible

    # Creats a HTML file in figures
    # fig.write_html(file_path)
    fig.show()


if __name__ == '__main__':
    main()