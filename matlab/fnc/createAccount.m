%
% createAccount - Create an account in database based on extracted feature,
%                 and some extra information from the enroller.
%
% Arguments:
%	template    - extracted template from the iris image.
%	mask        - extracted mask from the iris image.
%	name        - name of the enroller.
%	exinfo      - more information of the enroller.
%
% Output:
%	account     - account of the enroller stored in the database.
%
function account = createAccount(template, mask, name, exinfo)
%% Package the account of the enroller
account.template    = template;
account.mask        = mask;
account.name        = name;
account.exinfo		= exinfo;


%% Save to the account database
% Get file name for the account
files = dir('template-database/*.mat');
curNumfile = length(files);
filename = num2str(curNumfile+1);

% Save
save(['template-database/', filename, '.mat'], 'template', 'mask', 'name', 'exinfo')


end

