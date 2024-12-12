# ----- INSERTS -----
insertService = \
    "INSERT INTO services (name, token, write_token, js_parser_code) " \
    "VALUES (%s, %s, %s, %s) " \
    "RETURNING *"

insertStatistics = \
    "INSERT INTO statistics (service_write_token, text, value, bool) " \
    "VALUES (%s, %s, %s, %s) " \
    "RETURNING *"

# ----- SELECTS -----
selectAllServices = \
    "SELECT * FROM services " \
    "ORDER BY registered"

selectServiceByToken = \
    "SELECT * FROM services " \
    "WHERE token = %s"

selectStatisticsByServiceWriteToken = \
    "SELECT * FROM statistics " \
    "WHERE service_write_token = %s "\
    "ORDER BY datetime"

# ----- UPDATES -----
updateServiceNameByToken = \
    "UPDATE services SET " \
    "name = %s " \
    "js_parser_code = %s " \
    "WHERE token = %s " \
    "RETURNING *"

# ----- DELETES -----
deleteStatisticsByIdServiceToken = \
    "DELETE FROM statistics " \
    "WHERE id = %s AND " \
    "service_write_token = %s"

deleteServiceByToken = \
    "DELETE FROM services " \
    "WHERE token = %s"
