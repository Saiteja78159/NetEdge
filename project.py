import json
from bs4 import BeautifulSoup

# HTML content (replace this with your actual HTML content or fetch it using requests)
html_content = '''
<div id="tablePosition_wrapper" class="dataTables_wrapper no-footer"><div class="dataTables_length" id="tablePosition_length"><label>Show <select name="tablePosition_length" aria-controls="tablePosition" class="select2-hidden-accessible" tabindex="-1" aria-hidden="true"><option value="10">10</option><option value="25">25</option><option value="50">50</option><option value="100">100</option></select><span class="select2 select2-container select2-container--default" dir="ltr" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-labelledby="select2-tablePosition_length-2p-container"><span class="select2-selection__rendered" id="select2-tablePosition_length-2p-container" title="10">10</span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span> entries</label></div><div id="tablePosition_filter" class="dataTables_filter"><label>Search:<input type="search" class="" placeholder="" aria-controls="tablePosition"></label></div><table id="tablePosition" class="table table cell-border hover align-middle table-nowrap mb-0 dataTable no-footer" style="width: 100%;" aria-describedby="tablePosition_info">

    <thead class="table-light">
        <tr><th style="width: 72px;" class="sorting sorting_asc" tabindex="0" aria-controls="tablePosition" rowspan="1" colspan="1" aria-label="Position: activate to sort column descending" aria-sort="ascending">Position</th><th style="width: 106px;" class="sorting" tabindex="0" aria-controls="tablePosition" rowspan="1" colspan="1" aria-label="Qualifications : activate to sort column ascending">Qualifications </th><th class="sorting" tabindex="0" aria-controls="tablePosition" rowspan="1" colspan="1" aria-label="Experience Required : activate to sort column ascending" style="width: 100px;">Experience Required </th><th class="sorting" tabindex="0" aria-controls="tablePosition" rowspan="1" colspan="1" aria-label="Position Concept: activate to sort column ascending" style="width: 76px;">Position Concept</th><th class="action sorting" style="width: 187px;" tabindex="0" aria-controls="tablePosition" rowspan="1" colspan="1" aria-label="Actions: activate to sort column ascending">Actions</th></tr>
    </thead><tbody><tr class="odd"><td class="sorting_1">Digital Marketing Executive</td><td>Essential : MBA with Specialization in Marketing.   Desirable : English Literature Graduate or Diplo</td><td>Proven experience in digital marketing, in an ad or marketing agency, with a focus on social media, content creation, and SEO.
Experience in conceptualization and getting websites created by Developers.
Strong knowledge of digital marketing tools and platforms.
Excellent written and verbal communication skills.
Analytical mindset with the ability to interpret data and draw actionable insights.</td><td>As a Digital Marketing Executive at NetEdge, you will play a crucial role in developing and implementing digital marketing strategies to enhance our online presence and drive business growth. We are looking for a talented and motivated individual with a passion for digital marketing and a strong grasp of the latest trends and technologies.</td><td><div style="    display: flex;
    column-gap: 2px;"><button class="btn" onclick="applyForm(2,'Digital Marketing Executive')">Apply</button>
<button onclick="positionDetails(2)" class="btn">View</button></div></td></tr></tbody>

</table><div class="dataTables_info" id="tablePosition_info" role="status" aria-live="polite">Showing 1 to 1 of 1 entries</div><div class="dataTables_paginate paging_simple_numbers" id="tablePosition_paginate"><a class="paginate_button previous disabled" aria-controls="tablePosition" aria-disabled="true" role="link" data-dt-idx="previous" tabindex="-1" id="tablePosition_previous">Previous</a><span><a class="paginate_button current" aria-controls="tablePosition" role="link" aria-current="page" data-dt-idx="0" tabindex="0">1</a></span><a class="paginate_button next disabled" aria-controls="tablePosition" aria-disabled="true" role="link" data-dt-idx="next" tabindex="-1" id="tablePosition_next">Next</a></div></div>
'''

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table and rows
table = soup.find('table', {'id': 'tablePosition'})
rows = table.find_all('tr')[1:]  # Skip the header row

# Extract job data from each row
jobs = []
for row in rows:
    cols = row.find_all('td')
    job = {
        'Position': cols[0].text.strip(),
        'Qualifications': cols[1].text.strip(),
        'Experience Required': cols[2].text.strip(),
        'Position Concept': cols[3].text.strip(),
    }
    jobs.append(job)

# Save the data to a JSON file
with open('jobs.json', 'w') as f:
    json.dump(jobs, f, indent=4)

print("Job data saved to jobs.json")
