# -*- coding: utf-8 -*-
# rpcontacts/model.py

"""This module provides a model to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ContactsModel:
    """Class to create, add, delete, and clear contacts."""

    def __init__(self):
        self.model = self._create_model()

    @staticmethod
    def _create_model():
        """Create and set up the model.

        Returns:
            [QSqlTableModel]: model of tabel with defined headers.
        """
        table_model = QSqlTableModel()
        table_model.setTable("contacts")
        table_model.setEditStrategy(QSqlTableModel.OnFieldChange)
        table_model.select()
        headers = ("ID", "Name", "Job", "Email")
        for column_index, header in enumerate(headers):
            table_model.setHeaderData(column_index, Qt.Horizontal, header)
        return table_model

    def add_contact(self, data: list):
        """Add a contact to the database.

        Args:
            data (list): name, job, and email data
        """
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()

    def delete_contact(self, row: int):
        """Remove a contact from the database.

        Args:
            row (int): the row index
        """
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()

    def clear_contacts(self):
        """Remove all contacts in the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
