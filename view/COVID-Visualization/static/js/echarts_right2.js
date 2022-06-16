var echarts_right2 = echarts.init(document.getElementById('r2'), "dark");

// var ddd = [{'name': '肺炎', 'value': '12734670'}, {'name': '实时', 'value': '12734670'} ]
var echarts_right2_option = {
    // backgroundColor: '#515151',
  title: {
      text: '微博热榜',
      subtext: '',
      right:200,
      top:10
  },
  dataset: {
    source: []
  },
  grid: { containLabel: true },
  xAxis: { name: 'amount' },
  yAxis: { type: 'category' ,
            axisLabel: { interval: 0, rotate: 30 }},

  series: [
    {
      type: 'bar',
      encode: {
        // Map the "amount" column to X axis.
        x: 'num',
        // Map the "product" column to Y axis
        y: 'hotPoint'
      }
    }
  ]
}

echarts_right2.setOption(echarts_right2_option);
echarts_right2.on('click', function(params) {
    console.log(params.data[0])
    get_c2_data(params.data[0])
});
