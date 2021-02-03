% include('header.tpl')

<div class="columns">
  <div class="column is-2 menu">
    % include('sidebar.tpl')
  </div>

  <div class="column">

  %for item in res:
      {{item}}
      <br/>
  %end

  </div>
</div>

% include('footer.tpl')
