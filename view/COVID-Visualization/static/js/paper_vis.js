let papersInfo = [];
let locs = [];
let tippys = null;
let brush = null;

const sizes = {
  margins: {l: 20, b: 20, r: 20, t: 20},
};
const slct_papers_info = d3.select("#slct_papers_info");


const drawSize = () => {
  const co = document.getElementById("container");
  const win_height = Math.max(window.innerHeight - 200, 310);
  let win_width = Math.max(co.offsetWidth - 210, 300);
  if (co.offsetWidth < 768) ww = co.offsetWidth - 10.0;
  if (win_height / win_width > 1.3) {
    const min = Math.min(win_height, win_width);
    return [min, min];
  }
  return [win_width, win_height];
};


const xl = d3.scaleLinear().range([0, 500]);
const yl = d3.scaleLinear().range([0, 500]);
const scatters = d3.select(".scatters");
const g1 = scatters.append("g");
const g2 = scatters.append("g");
var wall = scatters.append("g")
var bottom = scatters.append("g")
var bottom1 = scatters.append("g")

const XScale = d3.scaleLinear().domain([-200, 200]).range([0, 1000])
const YScale = d3.scaleLinear().domain([-200, 200]).range([0, 600])

const brush_start = (slct) => {
  //tippys.forEach((tip) => tip.disable());
  //console.log(slct)
        bottom.selectAll('rect').remove()
        bottom.selectAll('text').remove()
        bottom1.selectAll('text').remove()
  brushed(slct);
};

const brushed = (slct) => {
  //确定矩形范围并每次选择一个新的矩形范围，矩形可调整位置并调整范围大小
  console.log("brushed")

};

function brush_ended(slct) {

  //tippys.forEach((tip) => tip.enable());
  //显示矩形围住的论文信息列表，且完成悬浮在每条信息上有提示框的功能（提示框中信息包含文章题目和作者）
  const slct_dots = [];
  const extentF = slct.selection[0];
  const extentL = slct.selection[1];

  console.log(slct.selection)

  newPapersInfo = papersInfo.filter(function(d){
    if(d.pos != null){
    return d.pos[0] >= extentF[0] && d.pos[0] <= extentL[0] && d.pos[1] >= extentF[1] && d.pos[1] <= extentL[1];
    }
  })

  console.log(newPapersInfo)
  let aaa = 0;

  for(aaa; aaa <= newPapersInfo.length; aaa++){
    bottom1.append("text")
    .attr("x", 40)
    .attr("y", 590 + aaa * 54)
    .attr("font-size", 19)
    .text(newPapersInfo[aaa].title)


    bottom.append("text")
    .attr("x", 40)
    .attr("y", 617 + aaa * 54)
    .attr("font-size", 17)
    .text("用户:" + newPapersInfo[aaa].authors + "……………………属地:" + newPapersInfo[aaa].location + "……………………热搜:" + newPapersInfo[aaa].hotPoint)

    bottom.append("rect")
    .attr("x", 40)
    .attr("y", 570 + aaa * 54)
    .attr("width", 1300)
    .attr("height", 50)
    .attr("fill", "black")
    .attr("opacity", 0.1)
  }
//      bottom.selectAll("rect")
//      .data(newPapersInfo.filter(function(d){
//        return d.pos != null
//      }),(d=>i))
//      .enter().append("rect")
//      .attr('x', 40)
//      .attr('y', 570 + i * 50)
//      .attr("width", 1000)
//      .attr("height", 48)
//      .attr("fill", "black")
//      .attr("opacity", 0.1)

//      .on("mouseover",function(i,d){
////        d3.selectAll(".dot")
////        .attr('opacity',0.2)
//        d3.select(this)
//        console.log(i)
//        console.log(d)
//        console.log(this)
//    })
  //在页面下方显示矩形框内的论文信息
  /*鼠标悬浮于点时 使点高亮 显示悬浮框信息
    .on("mouseenter", (slct, d) => {
      
    })*/

  /*鼠标离开点的时候取消点高亮 隐藏悬浮框信息
    .on("mouseleave", (slct, d) => {

      
  });*/
}

const draw_update = () => {{
      const [d_width, d_height] = drawSize();

      scatters.attr("width", d_width+ 400).attr("height", d_height + 770);
      d3.select("#info_items").style("height", `${d_height}px`);

      xl.range([sizes.margins.l, d_width - sizes.margins.r]);
      yl.range([sizes.margins.t, d_height - sizes.margins.b]);

      console.log(sizes.margins.l)
      console.log(d_width - sizes.margins.r)
      console.log(sizes.margins.t)
      console.log(d_height - sizes.margins.b)

      brush.extent([
        [0, 0],
        [d_width, d_height],
      ]);
      g1.call(brush);
      //console.log(papersInfo)
      locs = papersInfo.map((d) => {
        const r2 = d.is_selected ? 8 : 4;

        const [x, y] = [0, 0];
     if(d.pos != null){
      const [x, y] = [xl(d.pos[0]), yl(d.pos[1])];
      }

        //console.log([x, y])
        return new cola.Rectangle(x - r2, x + r2, y - r2, y + r2);
      })
      
      //画出散点，并且完成悬浮在每个点上有提示框的功能（提示框中信息包含文章题目和作者）

      scatters.selectAll("circle")
      .data(papersInfo.filter(function(d){
        return d.pos != null
      }))
      .enter().append("circle")
      .attr('cx', d => d.pos[0])
      .attr('cy', d => d.pos[1])
      .attr('r', 5)
      .attr('opacity', 0.5)
      .attr('fill', 'green')
      .on("mouseover",function(i,d){
//        d3.selectAll(".dot")
//        .attr('opacity',0.2)
        

        d3.select(this)
        .attr('fill',"red")
        console.log(d)
        console.log(d.title)

        wall.append("rect")
        .attr('x',d.pos[0] - 5)
        .attr('y',d.pos[1] - 30)
        .attr('width',700)
        .attr('height',70)
        .attr('opacity',0.2)
        .attr('fill',"black")

        wall.append("text")
          .attr('x',d.pos[0])
          .attr('y',d.pos[1])
          .attr('font-size', 21)
        //  .attr("fill", "white")
          .text(d.title)

        wall.append("text")
          .attr('x',d.pos[0])
          .attr('y',d.pos[1] + 30)
       //   .attr("fill","white")
          .attr('font-size', 15)
          .text("用户名：" + d.authors)

        wall.append("text")
          .attr('x',d.pos[0] + 260)
          .attr('y',d.pos[1] + 30)
       //   .attr("fill","white")
          .attr('font-size', 15)
          .text("属地：" + d.location)

      }).on("mouseout",function(){
        d3.select(this)
        .attr('fill',"green")
//        svg.selectAll(".dot")
//        .attr('opacity',1.0)
        wall.selectAll('rect').remove()
        wall.selectAll('text').remove()
      })


    }
};

const tooltip_template = (d) => `
    <div>
        <div class="tt-title">${d.title}</div>
        <p>${d.authors.join(", ")}</p>
    </div>
`;

const start = () => {
  //读数据文件，并设置文献代表的散点的位置
  Promise.all([
    $.get("origin_papers.json"),
    $.get("proje_papers.json"),
  ])
    .then(([origin, proj]) => {
      const projec = new Map();
      //将两个json数据通过id和uid进行连接，获取pos信息
      proj.forEach(d => {
      projec.set(d.id, d.pos)
      })

      //将x,y位置域映射到坐标轴上
      origin.forEach(d => {
      position = projec.get(d.UID)
      //console.log(position)
      if(position != null){
        d.pos = [XScale(position[0]), YScale(position[1])]
      }
      //console.log(d.pos)

      })
      papersInfo = origin;
      //console.log(papersInfo)
      draw_update();
    })
    .catch((e) => console.error(e));

  brush = d3
    .brush()
    .on("start", brush_start)
    .on("brush", brushed)
    .on("end", brush_ended);
};