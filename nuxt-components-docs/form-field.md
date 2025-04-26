<!-- source: https://ui.nuxt.com/components/form-field --> # FormField

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/FormField.vue)

A wrapper for form elements that provides validation and error handling.

## Usage

Wrap any form component with a FormField. Used in a [Form](/components/form),
it provides validation and error handling.

### Label

Use the `label` prop to set the label for the form control.

label

Email

    
    
    <template>
      <UFormField label="Email">
        <UInput placeholder="Enter your email" />
      </UFormField>
    </template>
    

The label `for` attribute and the form control are associated with a unique
`id` if not provided.

When using the `required` prop, an asterisk is be added next to the label.

required

true

Email

    
    
    <template>
      <UFormField label="Email" required>
        <UInput placeholder="Enter your email" />
      </UFormField>
    </template>
    

### Description

Use the `description` prop to provide additional information below the label.

description

Email

We'll never share your email with anyone else.

    
    
    <template>
      <UFormField label="Email" description="We'll never share your email with anyone else.">
        <UInput placeholder="Enter your email" class="w-full" />
      </UFormField>
    </template>
    

### Hint

Use the `hint` prop to display a hint message next to the label.

hint

EmailOptional

    
    
    <template>
      <UFormField label="Email" hint="Optional">
        <UInput placeholder="Enter your email" />
      </UFormField>
    </template>
    

### Help

Use the `help` prop to display a help message below the form control.

help

Email

Please enter a valid email address.

    
    
    <template>
      <UFormField label="Email" help="Please enter a valid email address.">
        <UInput placeholder="Enter your email" class="w-full" />
      </UFormField>
    </template>
    

### Error

Use the `error` prop to display an error message below the form control. When
used together with the `help` prop, the `error` prop takes precedence.

When used inside a [Form](/components/form), this is automatically set when a
validation error occurs.

error

Email

Please enter a valid email address.

    
    
    <template>
      <UFormField label="Email" error="Please enter a valid email address.">
        <UInput placeholder="Enter your email" class="w-full" />
      </UFormField>
    </template>
    

[](/getting-started/theme#colors)This sets the `color` to `error` on the form
control. You can change it globally in your `app.config.ts`.

### Size

Use the `size` prop to change the size of the FormField, the `size` is proxied
to the form control.

size

xl

EmailOptional

We'll never share your email with anyone else.

Please enter a valid email address.

    
    
    <template>
      <UFormField
        label="Email"
        description="We'll never share your email with anyone else."
        hint="Optional"
        help="Please enter a valid email address."
        size="xl"
      >
        <UInput placeholder="Enter your email" class="w-full" />
      </UFormField>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`name`| | ` string`The name of the FormField. Also used to match form errors.  
`errorPattern`| | ` RegExp`A regular expression to match form error names.  
`label`| | ` string`  
`description`| | ` string`  
`help`| | ` string`  
`error`| | ` string | false | true`  
`hint`| | ` string`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl"`  
`required`| | `boolean`  
`eagerValidation`| | `boolean`If true, validation on input will be active immediately instead of waiting for a blur event.  
`validateOnInputDelay`| `300`| ` number`Delay in milliseconds before
validating the form on input events.  
`ui`| | ` { root?: ClassNameValue; wrapper?: ClassNameValue; labelWrapper?: ClassNameValue; label?: ClassNameValue; container?: ClassNameValue; description?: ClassNameValue; error?: ClassNameValue; hint?: ClassNameValue; help?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`label`| `{ label?: string | undefined; }`  
`hint`| `{ hint?: string | undefined; }`  
`description`| `{ description?: string | undefined; }`  
`help`| `{ help?: string | undefined; }`  
`error`| `{ error?: string | boolean | undefined; }`  
`default`| `{ error?: string | boolean | undefined; }`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        formField: {
          slots: {
            root: '',
            wrapper: '',
            labelWrapper: 'flex content-center items-center justify-between',
            label: 'block font-medium text-default',
            container: 'mt-1 relative',
            description: 'text-muted',
            error: 'mt-2 text-error',
            hint: 'text-muted',
            help: 'mt-2 text-muted'
          },
          variants: {
            size: {
              xs: {
                root: 'text-xs'
              },
              sm: {
                root: 'text-xs'
              },
              md: {
                root: 'text-sm'
              },
              lg: {
                root: 'text-sm'
              },
              xl: {
                root: 'text-base'
              }
            },
            required: {
              true: {
                label: "after:content-['*'] after:ms-0.5 after:text-error"
              }
            }
          },
          defaultVariants: {
            size: 'md'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            formField: {
              slots: {
                root: '',
                wrapper: '',
                labelWrapper: 'flex content-center items-center justify-between',
                label: 'block font-medium text-default',
                container: 'mt-1 relative',
                description: 'text-muted',
                error: 'mt-2 text-error',
                hint: 'text-muted',
                help: 'mt-2 text-muted'
              },
              variants: {
                size: {
                  xs: {
                    root: 'text-xs'
                  },
                  sm: {
                    root: 'text-xs'
                  },
                  md: {
                    root: 'text-sm'
                  },
                  lg: {
                    root: 'text-sm'
                  },
                  xl: {
                    root: 'text-base'
                  }
                },
                required: {
                  true: {
                    label: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                }
              },
              defaultVariants: {
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            formField: {
              slots: {
                root: '',
                wrapper: '',
                labelWrapper: 'flex content-center items-center justify-between',
                label: 'block font-medium text-default',
                container: 'mt-1 relative',
                description: 'text-muted',
                error: 'mt-2 text-error',
                hint: 'text-muted',
                help: 'mt-2 text-muted'
              },
              variants: {
                size: {
                  xs: {
                    root: 'text-xs'
                  },
                  sm: {
                    root: 'text-xs'
                  },
                  md: {
                    root: 'text-sm'
                  },
                  lg: {
                    root: 'text-sm'
                  },
                  xl: {
                    root: 'text-base'
                  }
                },
                required: {
                  true: {
                    label: "after:content-['*'] after:ms-0.5 after:text-error"
                  }
                }
              },
              defaultVariants: {
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[FormA form component with built-in validation and submission
handling.](/components/form)[IconA component to display any icon from
Iconify.](/components/icon)

