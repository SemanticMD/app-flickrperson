# -*- coding: utf-8 -*-

# This file is part of PyBOSSA.
#
# PyBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBOSSA.  If not, see <http://www.gnu.org/licenses/>.

import requests
import json

def get_he_images(tag_name):
    output = None

    try:
        print('Contacting SemanticMD for images')
        my_url = "https://api.semantic.md/tag/" + tag_name

        r = requests.get(url=my_url)
        output = r.json()['tag_images']
        print('Data retrieved from SemanticMD')
    except:
        print('Data not retrieved!')
        return False

    # For each photo ID create its direct URL according to its size:
    # big, medium, small (or thumbnail) + Flickr page hosting the photo
    tasks = []
    headings = 'question,url_m,link,url_b'
    tasks.append(headings)
    question = 'Do you see an artifact in this image?'
    for img_url in output:
        img_url_clean = img_url.encode('utf-8')
        tasks.append(",".join([question, img_url_clean, img_url_clean, img_url_clean]))
    return tasks

if __name__ == '__main__':
    outfile = open('pbs_tasks.csv', 'w')
    tasks = get_he_images('dfs-present')
    print >> outfile, "\n".join(str(i) for i in tasks)
    outfile.close()
