import mysql.connector as mysql
import pandas as pd


def task1(conn):
    """Task 1: Retrieve the total number of tours in each tour type, sorted by the tour type name in ascending order."""

    query = """
        SELECT
            tour_type_name AS TourType,
            COUNT(tour_id) AS ToursNumber
        FROM
            tour_type INNER JOIN tour USING (tour_type_id)
        GROUP BY
            tour_type_name
        ORDER BY
            tour_type_name
    """

    return pd.read_sql(query, conn)


def task2(conn):
    """Task 2: Find the average tour price for each tour type, considering only tour types with more than 5 tours and display them in descending order of the average price."""

    query = """
        SELECT
            tour_type_name AS TourType,
            AVG(tour_price) AS AveragePrice,
            COUNT(tour_id) AS ToursNumber
        FROM
            tour_type INNER JOIN tour USING (tour_type_id)
        GROUP BY
            tour_type_name
        HAVING
            ToursNumber > 1
        ORDER BY
            AveragePrice DESC
    """

    return pd.read_sql(query, conn)


def task3(conn):
    """Task 3: Retrieve the total number of tours in each country, sorted by the total number of tours in descending order."""

    query = """
        SELECT
            tour_country AS Country,
            COUNT(tour_id) AS ToursNumber
        FROM
            tour
        GROUP BY
            tour_country
        ORDER BY
            ToursNumber DESC
    """

    return pd.read_sql(query, conn)


def task4(conn):
    """Task 4: Find the maximum tour price for each tour city and display the results in ascending order of the maximum price."""

    query = """
        SELECT
            tour_city AS City,
            MAX(tour_price) AS MaxPrice
        FROM
            tour
        GROUP BY
            tour_city
        ORDER BY
            MaxPrice
    """

    return pd.read_sql(query, conn)


def task5(conn):
    """Task 5: Retrieve the tour types and their average prices for tours with prices greater than $1000, sorted by the average price in descending order."""

    query = """
        SELECT
            tour_type_name AS TourType,
            AVG(tour_price) AS AveragePrice
        FROM
            tour_type INNER JOIN tour USING (tour_type_id)
        GROUP BY
            tour_type_name
        HAVING
            AveragePrice > 1000
        ORDER BY
            AveragePrice DESC
    """

    return pd.read_sql(query, conn)


def task6(conn):
    """Task 6: Find the tour types with the highest number of tours, considering only tour types with more than 10 tours, and display them in descending order of the tour count."""

    query = """
        SELECT
            tour_type_name AS TourType,
            COUNT(tour_id) AS ToursNumber
        FROM
            tour_type INNER JOIN tour USING (tour_type_id)
        GROUP BY
            tour_type_name
        HAVING
            ToursNumber > 1
        ORDER BY
            ToursNumber DESC
    """

    return pd.read_sql(query, conn)


def task7(conn):
    """Task 7: Retrieve the tour types and their minimum prices, considering only tour types with a minimum price greater than $500, sorted by the minimum price in ascending order."""

    query = """
        SELECT
            tour_type_name AS TourType,
            MIN(tour_price) AS MinPrice
        FROM
            tour_type INNER JOIN tour USING (tour_type_id)
        GROUP BY
            tour_type_name
        HAVING
            MinPrice > 500
        ORDER BY
            MinPrice
    """

    return pd.read_sql(query, conn)


def task8(conn):
    """Task 8: Find the average tour price for each country, considering only countries with more than 3 tours and display them in descending order of the average price."""

    query = """
        SELECT
            tour_country AS Country,
            AVG(tour_price) AS AveragePrice,
            COUNT(tour_id) AS ToursNumber
        FROM
            tour
        GROUP BY
            tour_country
        HAVING
            ToursNumber > 2
        ORDER BY
            AveragePrice DESC
    """

    return pd.read_sql(query, conn)


def main():
    conn = mysql.connect(
        host="localhost",
        database="tours_example",
        user="root",
        passwd=""
    )

    task_list = []
    task_list.append(task1(conn))
    task_list.append(task2(conn))
    task_list.append(task3(conn))
    task_list.append(task4(conn))
    task_list.append(task5(conn))
    task_list.append(task6(conn))
    task_list.append(task7(conn))
    task_list.append(task8(conn))

    for num in range(0, len(task_list)):
        task_list[num].to_csv(f"output/task{num + 1}.csv")

    conn.close()


if __name__ == "__main__":
    main()
