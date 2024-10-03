import csv
import pandas as pd
import matplotlib.pyplot as plt

def parse_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row
        data = [row for row in csv_reader]
    return header, data

def plot_access(filtered_df):
    pages = [int(row[0], 16) for row in filtered_df['Page'].values]
    plt.ylim(6.9999, 7.0001)

    #plt.hist(pages, bins='auto') 

    plt.scatter(range(len(pages)), pages)
    
    plt.xlabel('Index')
    plt.ylabel('Hexadecimal Page Address')
    plt.show()


    # addresses = [int(row[2], 16) for row in filtered_df.values]
    # # plt.ylim(1.84466*1e19, 1.844676*1e19)
    # # plt.ylim(1.84466771*1e19, 1.8446764*1e19)
    # plt.scatter(range(len(addresses)), addresses)
    # plt.xlabel('Index')
    # plt.ylabel('Hexadecimal Address')
    # plt.show()

if __name__ == "__main__":
    file_path = 'dbtest_event.csv'
    header, data = parse_csv(file_path)
    #data = data[:100]  # Parse only the first 100 rows
    
    # Create a DataFrame with all columns
    df = pd.DataFrame(data, columns=header)

    # Filter rows that have "Remote RAM" or "Local RAM" in the 5th column (index 4)
    filtered_df = df[(df.iloc[:, 4] == "Remote RAM") | (df.iloc[:, 4] == "Local RAM")]
    
    # filtered_df = filtered_df.iloc[:, [5, 6]]
    # filtered_df.columns = ["Access", "Address"]

    filtered_df = filtered_df.iloc[:, [6]]
    filtered_df.columns = ["Address"]

    filtered_df = filtered_df.sort_values(by='Address')

    filtered_df['Count'] = filtered_df.groupby('Address')['Address'].transform('count')

    # filtered_df['Page'] = filtered_df['Address'].apply(lambda x: x[:-3])
    # filtered_df['Page Count'] = filtered_df.groupby('Page')['Page'].transform('count')

    pgdf = pd.DataFrame()
    pgdf['Page'] = filtered_df['Address'].apply(lambda x: x[:-3])
    pgdf['Page Count'] = pgdf.groupby('Page')['Page'].transform('count')
    pgdf['Page Rank'] = range(1, len(pgdf) + 1)
    page_rank_map = {row['Page Rank']: row['Page'] for _, row in pgdf.iterrows()}
    print(page_rank_map)

    print(pgdf)
    # page_rank_map.plot()
    # plt.show()
    


    cache_df = pd.DataFrame()
    cache_df['Cacheline'] = pgdf['Page'].apply(lambda x: hex(int(x, 16) // 64))
    cache_df['Cache Count'] = cache_df.groupby('Cacheline')['Cacheline'].transform('count')
    cache_df['Cache Rank'] = range(1, len(cache_df) + 1)
    cache_rank_map = {row['Cache Rank']: row['Cacheline'] for _, row in cache_df.iterrows()}
    print(cache_df)


    # maxClm = filtered_df['Count'].max()
    # print("Max count is ",maxClm)
    # maxpClm = filtered_df['Page Count'].max()
    # print("Max Page count is ",maxpClm)
    
    #plot_access(pgdf)

    # Save the 7th column of filtered_df in results.csv
    # filtered_df.iloc[:, 6].to_csv('results.csv', index=False, header=False)
