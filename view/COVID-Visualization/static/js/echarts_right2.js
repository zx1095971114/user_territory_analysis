var echarts_right2 = echarts.init(document.getElementById('r2'), "dark");

// var ddd = [{'name': '肺炎', 'value': '12734670'}, {'name': '实时', 'value': '12734670'} ]
var echarts_right2_option = {
    // backgroundColor: '#515151',
    dataset: [
    {
      dimensions: ['hot_point','num'],
      source: [['Hannah Krause', 314],
        ['Zhao Qian', 351],
        ['Jasmin Krause ', 287],
        ['Li Lei', 219],
        ['Karle Neumann', 253],
        ['Mia Neumann', 165],
        ['Böhm Fuchs', 318],
        ['Han Meimei', 366]
    },
    {
      transform: {
        type: 'sort',
        config: { dimension: 'num', order: 'desc' }
      }
    }],
    xAxis: {
        type: 'category',
        axisLabel: { interval: 0, rotate: 30 }
    },
    yAxis: {},
    series: {
        type: 'bar',
        encode: { x: 'hot_point', y: 'num' },
        datasetIndex: 1
    }
}

echarts_right2.setOption(echarts_right2_option);