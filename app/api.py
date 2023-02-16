from flask import Flask
from app.netinfo import NetInfo
from prometheus_flask_exporter import PrometheusMetrics
from app.memory_info import MemoryInfo

app = Flask(__name__)

metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')


@app.route("/computer_name")
def computer_name():
    return MemoryInfo.get_computer_name()


@app.route("/cpu")
def cpu():
    return str(MemoryInfo.get_cpu_percent())


@app.route("/ram")
def ram():
    return str(MemoryInfo.get_ram_percent())


@app.route("/app_on_net")
@metrics.do_not_track()
def app_and_port():
    return print_html()


metrics.register_default(
    metrics.counter(
        'gru_ram_percentage', 'ram %',
        labels={'gru_ram_percentage': ram()}
    )
)


def print_html():
    table = []
    table.append("<table style=\"border: 1px solid black;\">\n")
    table.append("\t<tr>\n")
    td = []
    td.append(
        "<td style=\"border: 1px solid black;\">{0}</td>".format(
            "application name"))
    td.append("<td style=\"border: 1px solid black;\">{0}</td>".format("port"))
    td.append("<td style=\"border: 1px solid black;\">{0}</td>".format("ip"))
    table.append("\t\t" + "".join(td))
    table.append("\n\t</tr>\n")
    for i_app in NetInfo.get_app_usage_net():
        table.append("\t<tr style=\"border: 1px solid black;\">\n")
        td = []
        td.append(
            "<td style=\"border: 1px solid black;\">{0}</td>".format(
                i_app.app_name))
        td.append(
            "<td style=\"border: 1px solid black;\">{0}</td>".format(
                i_app.port))
        td.append(
            "<td style=\"border: 1px solid black;\">{0}</td>".format(
                i_app.ip))
        table.append("\t\t" + "".join(td))
        table.append("\n\t</tr>\n")

    table.append("</table>")
    return "".join(table)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
