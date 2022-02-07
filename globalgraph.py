#!/usr/bin/python3
import mg_python
import graphviz
import sys
if len(sys.argv)<2:
   print("Please pass the global to chart as a variable")
   sys.exit(1)
glbal=sys.argv[1]
print(glbal)
dot = graphviz.Digraph(comment='Global View')
dot
dot.node_attr.update(style='filled', color='lightgrey')
dot.node("A", glbal)
mg_python.m_set_host(0, "localhost", 7041, "", "")
key = mg_python.m_order(0, glbal, "")
cnt=0
cnt1=0
cnt2=0
cnt3=0
cnt4=0
while (key != ""):
   cnt=cnt+1
   dot.node("key_" + str(cnt),key + " , " + str(mg_python.m_get(0, glbal, key)))
   dot.edge("A","key_" + str(cnt))
   key1 = mg_python.m_order(0, glbal, key, "")
   while (key1 != ""):
      cnt1=cnt1+1
      dot.node("key1_" + str(cnt1),key1 + " , " + str(mg_python.m_get(0, glbal, key, key1))) 
      dot.edge("key_" + str(cnt),"key1_" + str(cnt1))
      key2 = mg_python.m_order(0, glbal, key, key1, "")
      while (key2 != ""):
         cnt2=cnt2+1
         dot.node("key2_" + str(cnt2),key2 + " , " + str(mg_python.m_get(0, glbal, key, key1, key2)))
         dot.edge("key1_" + str(cnt1),"key2_" + str(cnt2))
         key3 = mg_python.m_order(0, glbal, key, key1, key2, "")
         while (key3 != ""):
            cnt3=cnt3+1
            dot.node("key3_" + str(cnt3),key3 + " , " + str(mg_python.m_get(0, glbal, key, key1, key2, key3)))
            dot.edge("key2_" + str(cnt2),"key3_" + str(cnt3))
            key4 = mg_python.m_order(0, glbal, key, key1, key2, key3,"")
            while (key4 != ""):
               cnt4=cnt4+1
               yotstr=mg_python.m_get(0, glbal, key, key1, key2, key3, key4)
               dot.node("key4_" + str(cnt4),key4 + " , " + yotstr)
               dot.edge("key3_" + str(cnt3),"key4_" + str(cnt4))
               key4 = mg_python.m_order(0, glbal, key, key1, key2, key3, key4)
            key3 = mg_python.m_order(0, glbal, key, key1, key2, key3)
         key2 = mg_python.m_order(0, glbal, key, key1, key2) 
      key1  = mg_python.m_order(0, glbal, key, key1) 
   key  = mg_python.m_order(0, glbal, key)
print(dot.source)
dot.render('/var/srvbak/www/htdocs/Ram/global-' + glbal + '.gv').replace('\\', '/')
dot.render('/var/srvbak/www/htdocs/Ram/global-' + glbal + '.gv')
