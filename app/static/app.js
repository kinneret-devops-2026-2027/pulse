// Big Screen - the status page.   (Team 3 owns app/static/*)

async function getJSON(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(url + " -> " + r.status);
  return r.json();
}

function statusCell(status) {
  // MISSION (Team 3): return a coloured badge instead of plain text.
  //   up -> green, slow -> yellow, down -> red, unknown -> grey
  //   hint: '<span class="badge badge-' + status + '">' + status + '</span>'
  return status;
}

function renderSummary(results) {
  // MISSION (Team 3): show "X / Y services up" inside #summary
  document.getElementById("summary").textContent = "";
}

async function loadStatus() {
  const rows = document.getElementById("rows");
  rows.innerHTML = '<tr><td colspan="5">Checking…</td></tr>';
  try {
    const results = await getJSON("/api/status");
    rows.innerHTML = results.map(s => `
      <tr>
        <td><a href="${s.url}" target="_blank" rel="noopener">${s.name}</a></td>
        <td>${statusCell(s.status)}</td>
        <td>${s.http_status ?? "—"}</td>
        <td>${s.latency_ms != null ? s.latency_ms + " ms" : "—"}</td>
        <td>${s.checked_at.slice(11)}</td>
      </tr>`).join("");
    renderSummary(results);
  } catch (e) {
    rows.innerHTML = `<tr><td colspan="5">⚠️ ${e.message}</td></tr>`;
  }
}

async function loadMeta() {
  const v = await getJSON("/version");
  document.getElementById("version").textContent = `v${v.version} · ${v.commit} · ${v.env}`;
  const teams = await getJSON("/api/teams");
  document.getElementById("teams").innerHTML = teams.length
    ? teams.map(t => `<div class="team"><b>${t.emoji ?? "👥"} ${t.name}</b><span>${(t.members || []).join(" · ")}</span></div>`).join("")
    : "<p>No teams yet — add teams/team-N.json in your first PR!</p>";
}

document.getElementById("refresh").addEventListener("click", loadStatus);
loadMeta();
loadStatus();
