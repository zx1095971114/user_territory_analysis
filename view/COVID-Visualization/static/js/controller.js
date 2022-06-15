function get_c2_data() {
    $.ajax({
        url: "/c2",
        success: function (data) {
            echarts_center_option.series[0].data = data.data
            echarts_center.setOption(echarts_center_option)
        },
        error: console.error('请求c2数据失败')
    });
}

function get_l1_data() {
    echarts_left1.showLoading()
    $.ajax({
        url: "/l1",
        success: function (data) {
            echarts_left1_Option.xAxis[0].data = data.day
            echarts_left1_Option.series[0].data = data.confirm
            echarts_left1_Option.series[1].data = data.suspect
            echarts_left1_Option.series[2].data = data.heal
            echarts_left1_Option.series[3].data = data.dead
            echarts_left1.setOption(echarts_left1_Option)
            echarts_left1.hideLoading()
        },
        error: console.error('请求l1数据失败')
    });
}

function get_r1_data() {
    $.ajax({
        url: "/r1",
        success: function (data) {
            echarts_right1_option.xAxis.data = data.city;
            echarts_right1_option.series[0].data = data.confirm;
            echarts_right1.setOption(echarts_right1_option);
        },
        error: console.error('请求r1数据失败')
    })
}

function get_r2_data() {
    $.ajax({
        url: "/r2",
        success: function (data) {
            echarts_right2_option.series[0].data = data.kws;
            echarts_right2.setOption(echarts_right2_option);
        }
    })
}

function refreshPage() {
    window.location.reload()
}

get_c2_data()
get_r1_data()
get_r2_data()

// setInterval(get_c2_data, 10000 * 10)
// setInterval(get_r1_data, 10000 * 10)
// setInterval(get_r2_data, 1000 * 10)