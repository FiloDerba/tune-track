import polars as pl
from polars import DataFrame


def process_original_columns(df: DataFrame) -> DataFrame:
    df = df.with_columns(
        [
            # Parse the 'date' column into the proper Date format
            pl.col("date").str.strptime(pl.Date, format="%Y-%m-%d").alias("date"),
        ]
    )

    # Apply all other transformations in a second with_columns call
    df = df.with_columns(
        [
            # Create the 'is_weekend' column based on the weekday
            pl.col("date").dt.weekday().gt(4).cast(pl.Int8).alias("is_weekend"),

            # Create the 'season' column based on the month
            pl.when(pl.col("date").dt.month().is_in([12, 1, 2])).then(pl.lit("winter")).when(
                pl.col("date").dt.month().is_in([3, 4, 5])
            ).then(pl.lit("spring")).when(pl.col("date").dt.month().is_in([6, 7, 8])).then(
                pl.lit("summer")
            ).when(pl.col("date").dt.month().is_in([9, 10,
                                                    11])).then(pl.lit("autumn")).alias("season"),

            # Create time of day based on the hour
            pl.when(pl.col("hour_of_day").is_between(6, 11)).then(pl.lit("morning")).when(
                pl.col("hour_of_day").is_between(12, 17)
            ).then(pl.lit("afternoon")).when(pl.col("hour_of_day").is_between(18, 23)).then(
                pl.lit("evening")
            ).when(pl.col("hour_of_day").is_between(0,
                                                    5)).then(pl.lit("night")).alias("time_of_day"),

            # Create indicator for how long the song was played (1 very briefly to 5 fully)
            pl.when(pl.col("skip_1")).then(1).when(pl.col("skip_2")).then(2).when(
                pl.col("skip_3")
            ).then(3).when(pl.col("not_skipped")).then(5).otherwise(4).alias("song_completion"),

            # Create indicator for how long the user paused (0 no pause to 3 very long pause)
            pl.when(pl.col("no_pause_before_play") == 1).then(0).when(
                pl.col("short_pause_before_play") == 1
            ).then(1).when(pl.col("long_pause_before_play") == 1
                           ).then(2).otherwise(3).alias("pause_length_before_play")
        ]
    )

    df = df.drop(
        [
            "skip_1", "skip_2", "skip_3", "not_skipped", "no_pause_before_play",
            "short_pause_before_play", "long_pause_before_play"
        ]
    )

    return df
