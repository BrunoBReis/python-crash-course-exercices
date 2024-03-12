from die import Die
import plotly.express as px

file_path = 'python_project/data_visualization/figures/dice_visual_d6d10.html'

def main():

    # Create a D6 and D10
    die_1 = Die()
    die_2 = Die(10)

    # Make some rolls
    results = []
    for rull_num in range(50_000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # Analyze results
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    poss_results = range(2, max_result + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    # Visualize results
    title = "Results of rolling a D6 and D10 50000 times"
    labels = {'x': 'Result',
              'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    # Customization
    fig.update_layout(xaxis_dtick=1) # Every label is visible

    # Creats a HTML file in figures
    fig.write_html(file_path)


if __name__ == '__main__':
    main()
