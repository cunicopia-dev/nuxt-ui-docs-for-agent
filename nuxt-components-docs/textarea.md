<!-- source: https://ui.nuxt.com/components/textarea --> # Textarea

[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Textarea.vue)

A textarea element to input multi-line text.

## Usage

Use the `v-model` directive to control the value of the Textarea.

    
    
    <script setup lang="ts">
    const value = ref('')
    </script>
    
    <template>
      <UTextarea v-model="value" />
    </template>
    

### Rows

Use the `rows` prop to set the number of rows. Defaults to `3`.

rows

    
    
    <template>
      <UTextarea :rows="12" />
    </template>
    

### Placeholder

Use the `placeholder` prop to set a placeholder text.

placeholder

    
    
    <template>
      <UTextarea placeholder="Type something..." />
    </template>
    

### Autoresize

Use the `autoresize` prop to enable autoresizing the height of the Textarea.

autoresize

true

This is a long text that will autoresize the height of the Textarea.

    
    
    <script setup lang="ts">
    const value = ref('This is a long text that will autoresize the height of the Textarea.')
    </script>
    
    <template>
      <UTextarea v-model="value" autoresize />
    </template>
    

Use the `maxrows` prop to set the maximum number of rows when autoresizing. If
set to `0`, the Textarea will grow indefinitely.

maxrows

autoresize

true

This is a long text that will autoresize the height of the Textarea with a
maximum of 4 rows.

    
    
    <script setup lang="ts">
    const value = ref('This is a long text that will autoresize the height of the Textarea with a maximum of 4 rows.')
    </script>
    
    <template>
      <UTextarea v-model="value" :maxrows="4" autoresize />
    </template>
    

### Color

Use the `color` prop to change the ring color when the Textarea is focused.

color

neutral

highlight

true

    
    
    <template>
      <UTextarea color="neutral" highlight placeholder="Type something..." />
    </template>
    

The `highlight` prop is used here to show the focus state. It's used
internally when a validation error occurs.

### Variant

Use the `variant` prop to change the variant of the Textarea.

color

neutral

variant

subtle

highlight

false

    
    
    <template>
      <UTextarea color="neutral" variant="subtle" placeholder="Type something..." />
    </template>
    

### Size

Use the `size` prop to change the size of the Textarea.

size

xl

    
    
    <template>
      <UTextarea size="xl" placeholder="Type something..." />
    </template>
    

### Icon New

Use the `icon` prop to show an [Icon](/components/icon) inside the Textarea.

icon

size

md

variant

outline

rows

    
    
    <template>
      <UTextarea icon="i-lucide-search" size="md" variant="outline" placeholder="Search..." :rows="1" />
    </template>
    

Use the `leading` and `trailing` props to set the icon position or the
`leading-icon` and `trailing-icon` props to set a different icon for each
position.

trailingIcon

size

md

rows

    
    
    <template>
      <UTextarea trailing-icon="i-lucide-at-sign" placeholder="Enter your email" size="md" :rows="1" />
    </template>
    

### Avatar New

Use the `avatar` prop to show an [Avatar](/components/avatar) inside the
Textarea.

avatar.src

size

md

variant

outline

rows

![](https://github.com/nuxt.png)

    
    
    <template>
      <UTextarea
        :avatar="{
          src: 'https://github.com/nuxt.png'
        }"
        size="md"
        variant="outline"
        placeholder="Search..."
        :rows="1"
      />
    </template>
    

### Loading New

Use the `loading` prop to show a loading icon on the Textarea.

loading

true

trailing

false

rows

    
    
    <template>
      <UTextarea loading placeholder="Search..." :rows="1" />
    </template>
    

### Loading Icon New

Use the `loading-icon` prop to customize the loading icon. Defaults to
`i-lucide-refresh-cw`.

loading

true

loadingIcon

rows

    
    
    <template>
      <UTextarea loading loading-icon="i-lucide-repeat-2" placeholder="Search..." :rows="1" />
    </template>
    

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.loading` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.loading` key.

### Disabled

Use the `disabled` prop to disable the Textarea.

disabled

true

    
    
    <template>
      <UTextarea disabled placeholder="Type something..." />
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`id`| | ` string`  
`name`| | ` string`  
`placeholder`| | ` string`The placeholder text when the textarea is empty.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "ghost" | "none"`  
`size`| `'md'`| ` "xs" | "md" | "sm" | "lg" | "xl"`  
`required`| | `boolean`  
`autofocus`| | `boolean`  
`autofocusDelay`| `0`| ` number`  
`autoresize`| | `boolean`  
`autoresizeDelay`| `0`| ` number`  
`disabled`| | `boolean`  
`rows`| `3`| ` number`  
`maxrows`| `0`| ` number`  
`highlight`| | `boolean`Highlight the ring color like a focus state.  
`icon`| | ` string`Display an icon based on the `leading` and `trailing` props.  
`avatar`| | ` AvatarProps`Display an avatar on the left side.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "3xs" | "2xs" | "xs" | "md" | "sm" | "lg" | "xl" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`leading`| | `boolean`When `true`, the icon will be displayed on the left side.  
`leadingIcon`| | ` string`Display an icon on the left side.  
`trailing`| | `boolean`When `true`, the icon will be displayed on the right side.  
`trailingIcon`| | ` string`Display an icon on the right side.  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`modelValue`| | ` null | string | number`  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; leading?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; trailing?: ClassNameValue; trailingIcon?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
### Emits

Event |  Type   
---|---  
`blur`| `[event: FocusEvent]`  
`change`| `[event: Event]`  
`update:modelValue`| `[payload: string | number]`  
  
### Expose

When accessing the component via a template ref, you can use the following:

Name| Type  
---|---  
`textareaRef`| `Ref<HTMLTextAreaElement | null>`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        textarea: {
          slots: {
            root: 'relative inline-flex items-center',
            base: [
              'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
              'transition-colors'
            ],
            leading: 'absolute start-0 flex items-start',
            leadingIcon: 'shrink-0 text-dimmed',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            trailing: 'absolute end-0 flex items-start',
            trailingIcon: 'shrink-0 text-dimmed'
          },
          variants: {
            buttonGroup: {
              horizontal: {
                root: 'group',
                base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
              },
              vertical: {
                root: 'group',
                base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
              }
            },
            size: {
              xs: {
                base: 'px-2 py-1 text-xs gap-1',
                leading: 'ps-2 inset-y-1',
                trailing: 'pe-2 inset-y-1',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              sm: {
                base: 'px-2.5 py-1.5 text-xs gap-1.5',
                leading: 'ps-2.5 inset-y-1.5',
                trailing: 'pe-2.5 inset-y-1.5',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs',
                trailingIcon: 'size-4'
              },
              md: {
                base: 'px-2.5 py-1.5 text-sm gap-1.5',
                leading: 'ps-2.5 inset-y-1.5',
                trailing: 'pe-2.5 inset-y-1.5',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              lg: {
                base: 'px-3 py-2 text-sm gap-2',
                leading: 'ps-3 inset-y-2',
                trailing: 'pe-3 inset-y-2',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs',
                trailingIcon: 'size-5'
              },
              xl: {
                base: 'px-3 py-2 text-base gap-2',
                leading: 'ps-3 inset-y-2',
                trailing: 'pe-3 inset-y-2',
                leadingIcon: 'size-6',
                leadingAvatarSize: 'xs',
                trailingIcon: 'size-6'
              }
            },
            variant: {
              outline: 'text-highlighted bg-default ring ring-inset ring-accented',
              soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
              subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
              ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
              none: 'text-highlighted bg-transparent'
            },
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            leading: {
              true: ''
            },
            trailing: {
              true: ''
            },
            loading: {
              true: ''
            },
            highlight: {
              true: ''
            },
            type: {
              file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
            },
            autoresize: {
              true: {
                base: 'resize-none'
              }
            }
          },
          compoundVariants: [
            {
              color: 'primary',
              variant: [
                'outline',
                'subtle'
              ],
              class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
            },
            {
              color: 'primary',
              highlight: true,
              class: 'ring ring-inset ring-primary'
            },
            {
              color: 'neutral',
              variant: [
                'outline',
                'subtle'
              ],
              class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
            },
            {
              color: 'neutral',
              highlight: true,
              class: 'ring ring-inset ring-inverted'
            },
            {
              leading: true,
              size: 'xs',
              class: 'ps-7'
            },
            {
              leading: true,
              size: 'sm',
              class: 'ps-8'
            },
            {
              leading: true,
              size: 'md',
              class: 'ps-9'
            },
            {
              leading: true,
              size: 'lg',
              class: 'ps-10'
            },
            {
              leading: true,
              size: 'xl',
              class: 'ps-11'
            },
            {
              trailing: true,
              size: 'xs',
              class: 'pe-7'
            },
            {
              trailing: true,
              size: 'sm',
              class: 'pe-8'
            },
            {
              trailing: true,
              size: 'md',
              class: 'pe-9'
            },
            {
              trailing: true,
              size: 'lg',
              class: 'pe-10'
            },
            {
              trailing: true,
              size: 'xl',
              class: 'pe-11'
            },
            {
              loading: true,
              leading: true,
              class: {
                leadingIcon: 'animate-spin'
              }
            },
            {
              loading: true,
              leading: false,
              trailing: true,
              class: {
                trailingIcon: 'animate-spin'
              }
            }
          ],
          defaultVariants: {
            size: 'md',
            color: 'primary',
            variant: 'outline'
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
            textarea: {
              slots: {
                root: 'relative inline-flex items-center',
                base: [
                  'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                leading: 'absolute start-0 flex items-start',
                leadingIcon: 'shrink-0 text-dimmed',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailing: 'absolute end-0 flex items-start',
                trailingIcon: 'shrink-0 text-dimmed'
              },
              variants: {
                buttonGroup: {
                  horizontal: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
                  },
                  vertical: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
                  }
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leading: 'ps-2 inset-y-1',
                    trailing: 'pe-2 inset-y-1',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leading: 'ps-2.5 inset-y-1.5',
                    trailing: 'pe-2.5 inset-y-1.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leading: 'ps-2.5 inset-y-1.5',
                    trailing: 'pe-2.5 inset-y-1.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leading: 'ps-3 inset-y-2',
                    trailing: 'pe-3 inset-y-2',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leading: 'ps-3 inset-y-2',
                    trailing: 'pe-3 inset-y-2',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6'
                  }
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                leading: {
                  true: ''
                },
                trailing: {
                  true: ''
                },
                loading: {
                  true: ''
                },
                highlight: {
                  true: ''
                },
                type: {
                  file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
                },
                autoresize: {
                  true: {
                    base: 'resize-none'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  highlight: true,
                  class: 'ring ring-inset ring-primary'
                },
                {
                  color: 'neutral',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  highlight: true,
                  class: 'ring ring-inset ring-inverted'
                },
                {
                  leading: true,
                  size: 'xs',
                  class: 'ps-7'
                },
                {
                  leading: true,
                  size: 'sm',
                  class: 'ps-8'
                },
                {
                  leading: true,
                  size: 'md',
                  class: 'ps-9'
                },
                {
                  leading: true,
                  size: 'lg',
                  class: 'ps-10'
                },
                {
                  leading: true,
                  size: 'xl',
                  class: 'ps-11'
                },
                {
                  trailing: true,
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  trailing: true,
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  trailing: true,
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  trailing: true,
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  trailing: true,
                  size: 'xl',
                  class: 'pe-11'
                },
                {
                  loading: true,
                  leading: true,
                  class: {
                    leadingIcon: 'animate-spin'
                  }
                },
                {
                  loading: true,
                  leading: false,
                  trailing: true,
                  class: {
                    trailingIcon: 'animate-spin'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'outline'
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
            textarea: {
              slots: {
                root: 'relative inline-flex items-center',
                base: [
                  'w-full rounded-md border-0 placeholder:text-dimmed focus:outline-none disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                leading: 'absolute start-0 flex items-start',
                leadingIcon: 'shrink-0 text-dimmed',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                trailing: 'absolute end-0 flex items-start',
                trailingIcon: 'shrink-0 text-dimmed'
              },
              variants: {
                buttonGroup: {
                  horizontal: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-e-none group-not-only:group-last:rounded-s-none group-not-last:group-not-first:rounded-none'
                  },
                  vertical: {
                    root: 'group',
                    base: 'group-not-only:group-first:rounded-b-none group-not-only:group-last:rounded-t-none group-not-last:group-not-first:rounded-none'
                  }
                },
                size: {
                  xs: {
                    base: 'px-2 py-1 text-xs gap-1',
                    leading: 'ps-2 inset-y-1',
                    trailing: 'pe-2 inset-y-1',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  sm: {
                    base: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leading: 'ps-2.5 inset-y-1.5',
                    trailing: 'pe-2.5 inset-y-1.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs',
                    trailingIcon: 'size-4'
                  },
                  md: {
                    base: 'px-2.5 py-1.5 text-sm gap-1.5',
                    leading: 'ps-2.5 inset-y-1.5',
                    trailing: 'pe-2.5 inset-y-1.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  lg: {
                    base: 'px-3 py-2 text-sm gap-2',
                    leading: 'ps-3 inset-y-2',
                    trailing: 'pe-3 inset-y-2',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs',
                    trailingIcon: 'size-5'
                  },
                  xl: {
                    base: 'px-3 py-2 text-base gap-2',
                    leading: 'ps-3 inset-y-2',
                    trailing: 'pe-3 inset-y-2',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs',
                    trailingIcon: 'size-6'
                  }
                },
                variant: {
                  outline: 'text-highlighted bg-default ring ring-inset ring-accented',
                  soft: 'text-highlighted bg-elevated/50 hover:bg-elevated focus:bg-elevated disabled:bg-elevated/50',
                  subtle: 'text-highlighted bg-elevated ring ring-inset ring-accented',
                  ghost: 'text-highlighted bg-transparent hover:bg-elevated focus:bg-elevated disabled:bg-transparent dark:disabled:bg-transparent',
                  none: 'text-highlighted bg-transparent'
                },
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                leading: {
                  true: ''
                },
                trailing: {
                  true: ''
                },
                loading: {
                  true: ''
                },
                highlight: {
                  true: ''
                },
                type: {
                  file: 'file:me-1.5 file:font-medium file:text-muted file:outline-none'
                },
                autoresize: {
                  true: {
                    base: 'resize-none'
                  }
                }
              },
              compoundVariants: [
                {
                  color: 'primary',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                },
                {
                  color: 'primary',
                  highlight: true,
                  class: 'ring ring-inset ring-primary'
                },
                {
                  color: 'neutral',
                  variant: [
                    'outline',
                    'subtle'
                  ],
                  class: 'focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                },
                {
                  color: 'neutral',
                  highlight: true,
                  class: 'ring ring-inset ring-inverted'
                },
                {
                  leading: true,
                  size: 'xs',
                  class: 'ps-7'
                },
                {
                  leading: true,
                  size: 'sm',
                  class: 'ps-8'
                },
                {
                  leading: true,
                  size: 'md',
                  class: 'ps-9'
                },
                {
                  leading: true,
                  size: 'lg',
                  class: 'ps-10'
                },
                {
                  leading: true,
                  size: 'xl',
                  class: 'ps-11'
                },
                {
                  trailing: true,
                  size: 'xs',
                  class: 'pe-7'
                },
                {
                  trailing: true,
                  size: 'sm',
                  class: 'pe-8'
                },
                {
                  trailing: true,
                  size: 'md',
                  class: 'pe-9'
                },
                {
                  trailing: true,
                  size: 'lg',
                  class: 'pe-10'
                },
                {
                  trailing: true,
                  size: 'xl',
                  class: 'pe-11'
                },
                {
                  loading: true,
                  leading: true,
                  class: {
                    leadingIcon: 'animate-spin'
                  }
                },
                {
                  loading: true,
                  leading: false,
                  trailing: true,
                  class: {
                    trailingIcon: 'animate-spin'
                  }
                }
              ],
              defaultVariants: {
                size: 'md',
                color: 'primary',
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/textarea.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[TabsA set of tab panels that are displayed one at a
time.](/components/tabs)[ToastA succinct message to provide information or
feedback to the user.](/components/toast)

