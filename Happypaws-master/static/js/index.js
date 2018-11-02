  $(document).ready(function() {
    $('#contact_form').bootstrapValidator({
        // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            name: {
                validators: {
                        stringLength: {
                        min: 2,
                    },
                        notEmpty: {
                        message: 'Please enter your Name'
                    }
                }
            },
             location: {
                validators: {
                     stringLength: {
                        min: 2,
                    },
                    notEmpty: {
                        message: 'Please enter your Last Name'
                    }
                }
            },
			address: {
                validators: {
                     stringLength: {
                        min: 8,
			message: 'plese specify your address'
                    },
                    notEmpty: {
                        message: 'Please enter your address'
                    }
                }
            },
		
		
            description: {
                validators: {
                    notEmpty: {
                        message: 'Please enter the description'
                    },
                }
            },
            contact: {
                validators: {
                  stringLength: {
		
                        min: 10, 
                        max: 10,
                    notEmpty: {
                        message: 'Please enter your Contact No.'
                     }
                }
            },
                }
            }
        })
        .on('success.form.bv', function(e) {
            $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
         

            // Prevent form submission
            e.preventDefault();

            // Get the form instance
            var $form = $(e.target);

            // Get the BootstrapValidator instance
            var bv = $form.data('bootstrapValidator');

            // Use Ajax to submit form data
            $.post($form.attr('action'), $form.serialize(), function(result) {
                console.log(result);
            }, 'json');
        });
});
