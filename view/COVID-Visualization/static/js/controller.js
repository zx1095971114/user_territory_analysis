function get_c2_data(param) {
    $.ajax({
        type: "GET",
        url: "/c2",
        data: {
            "params":param
        },
        success: function (data) {
            echarts_center_option.series[0].data = data.data
            echarts_center.setOption(echarts_center_option)
        },
        error: console.error('请求c2数据失败')
    });
}

function get_r2_data() {
    $.ajax({
        url: "/r2",
        success: function (res) {
            echarts_right2_option.dataset.source = res.data;
            echarts_right2.setOption(echarts_right2_option);
        },
        error: console.error('请求r2数据失败')
    })
}

function refreshPage() {
    window.location.reload()
}

get_c2_data("all")
get_r2_data()

// setInterval(get_c2_data, 10000 * 10)
// setInterval(get_r1_data, 10000 * 10)
// setInterval(get_r2_data, 1000 * 10)