document.getElementById("simulateBtn").addEventListener("click", () => {
    const profit = parseFloat(document.getElementById("profit").value);
    const compute = parseFloat(document.getElementById("compute").value);
    const data = parseFloat(document.getElementById("data").value);
    const population = parseFloat(document.getElementById("population").value);
    const tau = parseFloat(document.getElementById("tau").value);

    const totalRevenue = profit + compute + data;

    const annualDividend = (tau * totalRevenue) / population;
    const monthlyDividend = annualDividend / 12;

    document.getElementById("annual").innerText =
        `Annual dividend per person: $${annualDividend.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;

    document.getElementById("monthly").innerText =
        `Monthly dividend per person: $${monthlyDividend.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
});
