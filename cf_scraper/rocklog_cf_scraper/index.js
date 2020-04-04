const ROCKFM_URL = 'https://rockfm.lt/dainu-paieska'
const ROCKLOG_DOMAIN = 'rocklog.pythonanywhere.com'
const UPLOAD_PATH = 'upload'

async function fetch_rockfm() {
  return fetch(ROCKFM_URL)
}

function split_out_entry(html) {
  const a = html.split('<div class="post_title">')[1]
  const b = a.split('</div>')[0]
  return b.trim()
}

function split_out_datetime(html) {
  const a = html.split('<div class="post_num">\n<p>')[1]
  const b = a.split('</p>\n</div>')[0]
  return b.trim()
}

// HTTPBasicAuth
async function send_to_rocklog(payload) {
  const user = ROCKLOG_UPLOAD_USERNAME
  const password = ROCKLOG_UPLOAD_PASSWORD

  const URL = `https://${user}:${password}@${ROCKLOG_DOMAIN}/${UPLOAD_PATH}/${payload}`
  console.log(URL)
  await fetch(URL)
}

async function handleRequest(request) {
  const a = await fetch_rockfm()
  const html = await a.text()

  const entry = split_out_entry(html)
  const datetime = split_out_datetime(html)

  const artist = entry.split(' - ')[0]
  const song = entry.split(' - ')[1]
  const date = datetime.split(' | ')[0]
  const hour = datetime.split(' | ')[1]

  const payload = `${artist}\n${song}\n${date}\n${hour}`
  const encoded = btoa(payload)

  await send_to_rocklog(encoded)
  
  return new Response(encoded, {
    headers: { 'content-type': 'text/plain' },
  })
}

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})