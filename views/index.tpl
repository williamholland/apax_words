% include('header.tpl')

<section class="section">
  <div class="columns is-widescreen">
    <div class="column is-half">
    <div class="notification is-light">
    <div class="container px-4">

      <h1 class="title has-text-danger">APAX Vocab</h1>

        <p class="subtitle">
          Words for hang-man, word-searches, bingo, charades or pictionary!
        </p>


        <form action=".">

          <label class="label" for="level">Level</label>
          <span class="select mb-4">
            <select id="level" name="level">
              %for level in levels:
                <option value="{{level}}">{{level}}</option>
              %end
            </select>
          </span>

          <label for="level" class="label">Quantity</label>
          <input style="width: 100px;" type="number" class="input mb-4" id="quantity" name="quantity" min="1" value="10" step="1">

          <br>

          <input type="submit" value="Get words" class="button is-link is-large is-fullwidth">

        </form>

        <p class="help mt-4">

          This website is designed for APAX April teachers. It will give a
          random sample of words taken from all of the lessons in a given
          level. The words are random each time, refreshing the page will give
          a different list of words. Students should have seen all of these
          words by the end of B3. Select which level you want words from, then
          you can change how many words you want, even hundreds!

        </p>

        <p class="help mt-4 has-text-right">

          By Will Holland.

        </p>
      </div>
      </div>
      </div>
    </div>
</section>

% include('footer.tpl')
