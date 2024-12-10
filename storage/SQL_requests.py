# ----- INSERTS -----
insertService = \
    "INSERT INTO services (name, token) " \
    "VALUES (%s, %s) " \
    "RETURNING *"

insertStatistics = \
    "INSERT INTO statistics (service_token, text, value) " \
    "VALUES (%s, %s, %s) " \
    "RETURNING *"

# ----- SELECTS -----
selectAllServices = \
    "SELECT * FROM services " \
    "ORDER BY registration_datetime"

selectServiceByToken = \
    "SELECT * FROM services " \
    "WHERE token = %s"

selectStatisticsByServiceToken = \
    "SELECT * FROM statistics " \
    "WHERE service_token = %s "\
    "ORDER BY datetime"

# ----- UPDATES -----
updateServiceNameByToken = \
    "UPDATE services SET " \
    "name = %s " \
    "WHERE token = %s " \
    "RETURNING *"

# ----- DELETES -----
deleteStatisticsById = \
    "DELETE FROM statistics " \
    "WHERE id = %s"

deleteServiceByToken = \
    "DELETE FROM services " \
    "WHERE token = %s"
