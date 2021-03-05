import matplotlib.pyplot as plt
import seaborn as sns


def showMissingDataGraph(df):
    plt.figure(figsize=(10, 5))
    sns.heatmap(df.isnull())
    plt.title("Missing Data", fontsize=20)
    plt.show()


def movieLengthGraph(top_content, total_content, barWidth=0.5):
    plt.figure(figsize=(10, 5))
    plt.bar(top_content.index, top_content, color='r', width=barWidth, label='Top 500')
    plt.bar([x+barWidth for x in total_content.index], total_content, color='g', width=barWidth, label='Total Entries')
    plt.ylabel('No. of Movies', fontweight='bold')
    plt.xlabel('Minutes', fontweight='bold')
    plt.title("Duration of Movies", fontsize=20)
    plt.legend()
    plt.show()


def tvShowLengthGraph(top_content, total_content, barWidth=0.5):
    plt.figure(figsize=(10, 5))
    plt.bar(top_content.index, top_content, color='r', width=barWidth, label='Top 500')
    plt.bar([x+barWidth for x in total_content.index], total_content, color='g', width=barWidth, label='Total Entries')
    plt.ylabel('No. of TV Shows', fontweight='bold')
    plt.xlabel('Seasons', fontweight='bold')
    plt.xticks([i+barWidth-0.25 for i in range(1, 16)], [i for i in range(1, 16)])
    plt.legend()
    plt.title("Duration of TV Shows", fontsize=20)
    plt.show()


def TypeRatio(df):
    plt.figure(figsize=(10, 5))
    plt.pie(df['type'].value_counts(), labels=df['type'].value_counts().index,
            explode=[0.05, 0], autopct='%1.2f%%', colors=['Orange', 'Red'])
    plt.title("Top Content Ratio", fontsize=20)
    plt.show()


def showGenreRatio(genre_percentage, Title):
    plt.figure(figsize=(10, 7))
    plt.pie(genre_percentage[1], labels=genre_percentage[0], autopct='%1.2f%%', colors=sns.color_palette("RdGy", n_colors=20))
    plt.title(f"{Title} Genre Ratio's", fontsize=20)
    plt.show()


def monthlyAnalysisGraph(total_content, top_content, barWidth=0.5):
    top_month_count = top_content['month_added'].value_counts().sort_index()
    total_month_count = total_content['month_added'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(total_month_count.index, total_month_count, color='r', label='Total Entries')
    plt.plot([x + barWidth for x in top_month_count.index], top_month_count, color='g', label='Top 500')
    plt.xlabel('Month', fontweight='bold')
    plt.ylabel('No. of Shows Released', fontweight='bold')
    plt.title("Shows added on Netflix on basis of Month (2008 - 2020)", fontsize=20)
    plt.xticks([r for r in range(1, 13)], ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'])
    plt.legend()
    plt.show()
