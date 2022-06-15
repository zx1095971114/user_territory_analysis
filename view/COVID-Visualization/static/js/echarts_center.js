var echarts_center = echarts.init(document.getElementById('c2'), "dark");

var echarts_center_option = {
    title: {
        text: '全国评论分布',
        subtext: '',
        x: 'left'
    },

    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'bottom',
        textStyle: {
            fontSize: 8,
        },
        splitList: [{
            start: 0,
            end: 15
        }, {
            start: 16,
            end: 40
        }, {
            start: 41,
            end: 80
        }, {
            start: 81,
            end: 150
        }, {
            start: 151
        }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: '评论人数',
        type: 'map',
        mapType: 'china',
        roam: false, //拖动和缩放
        itemStyle: {
            normal: {
                borderWidth: .5, //区域边框宽度
                borderColor: '#62d3ff', //区域边框颜色
                areaColor: "#b7ffe6", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .5,
                borderColor: '#fff',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 8,
            },
            emphasis: {
                show: true,
                fontSize: 8,
            }
        },
        data: [] //mydata 
    }]
};

echarts_center.setOption(echarts_center_option)