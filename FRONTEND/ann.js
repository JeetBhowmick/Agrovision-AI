document.getElementById("predictBtn").addEventListener("click", async () => {

  const data = {
    N: parseFloat(document.getElementById("N").value),
    P: parseFloat(document.getElementById("P").value),
    K: parseFloat(document.getElementById("K").value),
    temperature: parseFloat(document.getElementById("temperature").value),
    humidity: parseFloat(document.getElementById("humidity").value),
    ph: parseFloat(document.getElementById("ph").value),
    rainfall: parseFloat(document.getElementById("rainfall").value)
  };

  for (let key in data) {
    if (isNaN(data[key])) {
      alert("Please fill all fields correctly");
      return;
    }
  }

  const response = await fetch("http://127.0.0.1:5000/api/crop-recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await response.json();

  let html = "<h3>Top Crop Recommendations</h3><ul>";
  result.recommendations.forEach(r => {
    html += `<li><b>${r.crop}</b> — ${r.confidence}%</li>`;
  });
  html += "</ul>";

  document.getElementById("result").innerHTML = html;
});
