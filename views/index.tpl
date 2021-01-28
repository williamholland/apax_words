% include('header.tpl')

<h1>APAX Vocab</h1>

<form action=".">
  <label for="level">I want</label>
  <input type="number" id="quantity" name="quantity" min="1" value="10" step="1">
  <label for="level">words from</label>
  <select id="level" name="level">
    %for level in levels:
      <option value="{{level}}">{{level}}</option>
    %end
  </select>
  <label for="level">.</label>
  <br><br>
  <input type="submit" value="Get words!">
</form>
