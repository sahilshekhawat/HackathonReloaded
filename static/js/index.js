function random(name) {
  var value = 0,
      values = [],
      i = 0,
      last;
  return context.metric(function(start, stop, step, callback) {
    start = +start, stop = +stop;
    if (isNaN(last)) last = start;
    while (last < stop) {
      last += step;
      values = 2//abc();
      console.log("%%%%%%%%%%%%%%%%%");
      //value = 2;  //
      console.log(Math.max(-10, Math.min(10, value + .8 * Math.random() - .4 + .2 * Math.cos(i += .2))).toString());
      values.push(value);
    }
    callback(null, values = values.slice((start - stop) / step));
  }, name);
}

function abc() {
    $.ajax({
         type: 'GET',
         url: '/cpu/',
         data: '',
         success: function (data) {
            console.log(data);
            return parseInt(JSON.parse(data.content));
            //return json;
         }
     });
}

var context = cubism.context()
    .serverDelay(30)
    .clientDelay(0)
    .step(1e3)
    .size(960);

var ram = random("RAM (MiB)"),
    cpu = random("CPU "),
    processes = random("PROCESSES"),
    load = random("LOAD");


console.log(ram);

d3.select("#sysinfo").call(function(div) {
  div.append("div")
      .attr("class", "axis")
      .call(context.axis().orient("top"));

  div.selectAll(".horizon")
      .data([cpu, ram, processes, load])
    .enter().append("div")
      .attr("class", "horizon")
      .call(context.horizon().extent([-20, 20]));

  div.append("div")
      .attr("class", "rule")
      .call(context.rule());

});

// On mousemove, reposition the chart values to match the rule.
context.on("focus", function(i) {
  d3.selectAll(".value").style("right", i == null ? null : context.size() - i + "px");
});
