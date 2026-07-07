import matplotlib.pyplot as plt


def create_pie_chart(recommendations):

    labels = list(recommendations.keys())
    sizes = list(recommendations.values())

    plt.figure(figsize=(6, 6))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Recommended Asset Allocation")

    plt.savefig("static/allocation_chart.png")

    plt.close()