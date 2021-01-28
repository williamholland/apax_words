% include('header.tpl')

<h1>APAX Vocab</h1>

<form action="/words/">
  <label for="level">Level:</label>
  <select id="level" name="level">
    %for level in levels:
      <option value="{{level}}">{{level}}</option>
    %end
  </select>
  <br>
  <label for="level">Number of words:</label>
  <input type="number" id="quantity" name="quantity" min="1" value="10" step="1">
  <br>
  <input type="submit" value="Submit">
</form>
