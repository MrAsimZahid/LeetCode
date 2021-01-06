<h2>627. Swap Salary</h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__3Su4"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Given a table <code>salary</code>, such as the one below, that has m=male and f=female values. Swap all f and m values (i.e., change all f values to m and vice versa) with a <strong>single update statement</strong> and no intermediate temp table.</p>

<p>Note that you must write a single update statement, <strong>DO NOT</strong> write any select statement for this problem.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
</pre>
After running your <strong>update</strong> statement, the above salary table should have the following rows:

<pre>| id | name | sex | salary |
|----|------|-----|--------|
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
</pre>
</div>