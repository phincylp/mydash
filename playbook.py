#!/usr/bin/python

from utils import template

def play_message():
	print ("""
    <br>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6 col-md-offset-3">
                <h3 class="text-danger">
                    How to add your Host to the dashboard
                </h3>

                <ul>
                    <li>Go to <a style="text-decoration:none;" href="https://mydash.nm.domain.com/mydash/addhost.py">Add my Host </a></li>
                    <li>Enter your mysql server hostname and cluster name  in the input boxes. The cluster anme neds to be unique for a given cluster</li>
                    <li>Click on the Submit button and we will take care of the rest</li>
		    <li>Check if your host appears in the dashboard in some time </li>
                </ul>

                <br/>

            </div>
        </div>
    </div>
    """)


if __name__ == "__main__":
	template.print_header()
	play_message()
	template.print_footer()




