# -*- coding: utf-8 -*-
# rpcontacts/database.py

"""This module provies a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def create_connection(database_name: str):
    """Create and open a database connection.

    Args:
        database_name (str): name of the database

    Returns:
        [Boolean]: True if connection is made, False otherwise.
    """
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(database_name)

    if not connection.open():
        QMessageBox.warning(
            None, "RP Contact", f"Database Error: {connection.lastError().text()}"
        )
        return False

    _create_contacts_table()
    return True


def _create_contacts_table():
    """Create the contacts table in the database."""
    create_table_query = QSqlQuery()
    return create_table_query.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )
