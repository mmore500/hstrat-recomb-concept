import glob
import pandas as pd

def concat_dataframes_from_glob(glob_expression: str) -> pd.DataFrame:
    """
    Concatenate all CSV files matching a glob expression into a single DataFrame.

    Parameters
    ----------
    glob_expression : str
        A glob expression representing a list of files to read.

    Returns
    -------
    pd.DataFrame
        The concatenated DataFrame.
    """

    # Get a list of all files that match the glob expression
    filenames = glob.glob(glob_expression)

    # Create a list to store all dataframes
    dataframes = []

    # For each filename
    for filename in filenames:
        # Read the file into a dataframe
        df = pd.read_csv(filename)

        # Append the dataframe to the list
        dataframes.append(df)

    # Concatenate all dataframes along the row axis (i.e., one below another)
    combined_df = pd.concat(dataframes, axis=0, ignore_index=True)

    # Return the combined dataframe
    return combined_df
