cat /home/vtrqk/python/2021-1-MAILRU-SDET-Python-P-Smirnov/homework5/access.log |  awk ' 
{
temp = substr($6, 2)
if (temp == "GET")
        {
                get_count +=1t
        }

else if (temp == "POST")
        {
                post_count +=1
        }
} 
END {print "Result GET count:", get_count, "Result POST count: ", post_count}
'
