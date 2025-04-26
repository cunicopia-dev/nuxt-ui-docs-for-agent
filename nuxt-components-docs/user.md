<!-- source: https://ui.nuxt.com/components/user --> # UserPRO

[GitHub](https://github.com/nuxt/ui-
pro/blob/v3/src/runtime/components/User.vue)

Display user information with name, description and avatar.

## Usage

### Name

Use the `name` prop to display a name for the user.

name

John Doe

    
    
    <template>
      <UUser name="John Doe" />
    </template>
    

### Description

Use the `description` prop to display a description for the user.

name

description

John Doe

Software Engineer

    
    
    <template>
      <UUser name="John Doe" description="Software Engineer" />
    </template>
    

### Avatar

Use the `avatar` prop to display an [Avatar](/components/avatar) component.

avatar.src

avatar.icon

![John Doe](https://i.pravatar.cc/150?u=john-doe)

John Doe

Software Engineer

    
    
    <template>
      <UUser
        name="John Doe"
        description="Software Engineer"
        :avatar="{
          src: 'https://i.pravatar.cc/150?u=john-doe',
          icon: 'i-lucide-image'
        }"
      />
    </template>
    

Show all avatar properties

Prop |  Default |  Type   
---|---|---  
`src`| | ` string`  
`alt`| | ` string`  
`icon`| | ` string`  
`text`| | ` string`  
`ui`| | ` { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`  
  
### Chip

Use the `chip` prop to display a [Chip](/components/chip) component.

chip.color

primary

chip.position

top-right

![John Doe](https://i.pravatar.cc/150?u=john-doe)

John Doe

Software Engineer

    
    
    <template>
      <UUser
        name="John Doe"
        description="Software Engineer"
        :avatar="{
          src: 'https://i.pravatar.cc/150?u=john-doe'
        }"
        :chip="{
          color: 'primary',
          position: 'top-right'
        }"
      />
    </template>
    

Show all chip properties

Prop |  Default |  Type   
---|---|---  
`text`| | ` string | number`Display some text inside the chip.  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`position`| `'top-right'`| ` "top-right" | "bottom-right" | "top-left" | "bottom-left"`The position of the chip.  
`inset`| `false`| `boolean`When `true`, keep the chip inside the component for
rounded elements.  
`show`| `true`| `boolean`  
`ui`| | ` { root?: ClassNameValue; base?: ClassNameValue; }`  
  
### Size

Use the `size` prop to change the size of the user avatar and text.

size

xl

![John Doe](https://i.pravatar.cc/150?u=john-doe)

John Doe

Software Engineer

    
    
    <template>
      <UUser
        name="John Doe"
        description="Software Engineer"
        :avatar="{
          src: 'https://i.pravatar.cc/150?u=john-doe'
        }"
        chip
        size="xl"
      />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation. Defaults to
`horizontal`.

orientation

vertical

name

description

![John Doe](https://i.pravatar.cc/150?u=john-doe)

John Doe

Software Engineer

    
    
    <template>
      <UUser
        orientation="vertical"
        name="John Doe"
        description="Software Engineer"
        :avatar="{
          src: 'https://i.pravatar.cc/150?u=john-doe'
        }"
      />
    </template>
    

### Link

You can pass any property from the
[`<NuxtLink>`](https://nuxt.com/docs/api/components/nuxt-link) component such
as `to`, `target`, `rel`, etc.

![Nuxt UI Pro](https://github.com/nuxt-ui-pro.png)

[](https://github.com/nuxt/ui-pro)

Nuxt UI Pro

Premium components for Vue

    
    
    <template>
      <UUser
        to="https://github.com/nuxt/ui-pro"
        target="_blank"
        name="Nuxt UI Pro"
        description="Premium components for Vue"
        :avatar="{
          src: 'https://github.com/nuxt-ui-pro.png'
        }"
      />
    </template>
    

The `NuxtLink` component will inherit all other attributes you pass to the
`User` component.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`  
`size`| `'md'`| ` "md" | "xs" | "sm" | "lg" | "xl" | "3xs" | "2xs" | "2xl" | "3xl"`  
`target`| | ` null | "_blank" | "_parent" | "_self" | "_top" | string & {}`  
`to`| | ` string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Show properties

  * `name?: RouteRecordNameGeneric`
  * `params?: RouteParamsRawGeneric`
  * `path?: undefined`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>
  * `path: string`A relative path to the current location. This property should be removed
  * `query?: LocationQueryRaw`
  * `hash?: string`
  * `force?: boolean`Triggers the navigation even if the location is the same as the current one. Note this will also add a new entry to the history unless `replace: true` is passed.
  * `state?: HistoryState`State to save using the History API. This cannot contain any reactive values and some primitives like Symbols are forbidden. More info at <https://developer.mozilla.org/en-US/docs/Web/API/History/state>

  
`description`| | ` string`  
`name`| | ` string`  
`avatar`| | ` Omit<AvatarProps, "size"> & { [key: string]: any; }`Show properties

  * `icon?: string`
  * `class?: any`
  * `style?: any`
  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`
  * `src?: string`
  * `alt?: string`
  * `text?: string`

  
`chip`| | `boolean | Omit<ChipProps, "size" | "inset">`  
`ui`| | ` { root?: ClassNameValue; wrapper?: ClassNameValue; name?: ClassNameValue; description?: ClassNameValue; avatar?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`avatar`| `{}`  
`name`| `{}`  
`description`| `{}`  
`default`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        user: {
          slots: {
            root: 'relative group/user',
            wrapper: '',
            name: 'font-medium',
            description: 'text-muted',
            avatar: 'shrink-0'
          },
          variants: {
            orientation: {
              horizontal: {
                root: 'flex items-center'
              },
              vertical: {
                root: 'flex flex-col'
              }
            },
            to: {
              true: {
                name: [
                  'text-default peer-hover:text-highlighted',
                  'transition-colors'
                ],
                description: [
                  'peer-hover:text-toned',
                  'transition-colors'
                ],
                avatar: 'transform transition-transform duration-200 group-hover/user:scale-115'
              },
              false: {
                name: 'text-highlighted',
                description: ''
              }
            },
            size: {
              '3xs': {
                root: 'gap-1',
                wrapper: 'flex items-center gap-1',
                name: 'text-xs',
                description: 'text-xs'
              },
              '2xs': {
                root: 'gap-1.5',
                wrapper: 'flex items-center gap-1.5',
                name: 'text-xs',
                description: 'text-xs'
              },
              xs: {
                root: 'gap-1.5',
                wrapper: 'flex items-center gap-1.5',
                name: 'text-xs',
                description: 'text-xs'
              },
              sm: {
                root: 'gap-2',
                name: 'text-xs',
                description: 'text-xs'
              },
              md: {
                root: 'gap-2',
                name: 'text-sm',
                description: 'text-xs'
              },
              lg: {
                root: 'gap-2.5',
                name: 'text-sm',
                description: 'text-sm'
              },
              xl: {
                root: 'gap-2.5',
                name: 'text-base',
                description: 'text-sm'
              },
              '2xl': {
                root: 'gap-3',
                name: 'text-base',
                description: 'text-base'
              },
              '3xl': {
                root: 'gap-3',
                name: 'text-lg',
                description: 'text-base'
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
          uiPro: {
            user: {
              slots: {
                root: 'relative group/user',
                wrapper: '',
                name: 'font-medium',
                description: 'text-muted',
                avatar: 'shrink-0'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'flex items-center'
                  },
                  vertical: {
                    root: 'flex flex-col'
                  }
                },
                to: {
                  true: {
                    name: [
                      'text-default peer-hover:text-highlighted',
                      'transition-colors'
                    ],
                    description: [
                      'peer-hover:text-toned',
                      'transition-colors'
                    ],
                    avatar: 'transform transition-transform duration-200 group-hover/user:scale-115'
                  },
                  false: {
                    name: 'text-highlighted',
                    description: ''
                  }
                },
                size: {
                  '3xs': {
                    root: 'gap-1',
                    wrapper: 'flex items-center gap-1',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  '2xs': {
                    root: 'gap-1.5',
                    wrapper: 'flex items-center gap-1.5',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  xs: {
                    root: 'gap-1.5',
                    wrapper: 'flex items-center gap-1.5',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  sm: {
                    root: 'gap-2',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  md: {
                    root: 'gap-2',
                    name: 'text-sm',
                    description: 'text-xs'
                  },
                  lg: {
                    root: 'gap-2.5',
                    name: 'text-sm',
                    description: 'text-sm'
                  },
                  xl: {
                    root: 'gap-2.5',
                    name: 'text-base',
                    description: 'text-sm'
                  },
                  '2xl': {
                    root: 'gap-3',
                    name: 'text-base',
                    description: 'text-base'
                  },
                  '3xl': {
                    root: 'gap-3',
                    name: 'text-lg',
                    description: 'text-base'
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
          uiPro: {
            user: {
              slots: {
                root: 'relative group/user',
                wrapper: '',
                name: 'font-medium',
                description: 'text-muted',
                avatar: 'shrink-0'
              },
              variants: {
                orientation: {
                  horizontal: {
                    root: 'flex items-center'
                  },
                  vertical: {
                    root: 'flex flex-col'
                  }
                },
                to: {
                  true: {
                    name: [
                      'text-default peer-hover:text-highlighted',
                      'transition-colors'
                    ],
                    description: [
                      'peer-hover:text-toned',
                      'transition-colors'
                    ],
                    avatar: 'transform transition-transform duration-200 group-hover/user:scale-115'
                  },
                  false: {
                    name: 'text-highlighted',
                    description: ''
                  }
                },
                size: {
                  '3xs': {
                    root: 'gap-1',
                    wrapper: 'flex items-center gap-1',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  '2xs': {
                    root: 'gap-1.5',
                    wrapper: 'flex items-center gap-1.5',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  xs: {
                    root: 'gap-1.5',
                    wrapper: 'flex items-center gap-1.5',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  sm: {
                    root: 'gap-2',
                    name: 'text-xs',
                    description: 'text-xs'
                  },
                  md: {
                    root: 'gap-2',
                    name: 'text-sm',
                    description: 'text-xs'
                  },
                  lg: {
                    root: 'gap-2.5',
                    name: 'text-sm',
                    description: 'text-sm'
                  },
                  xl: {
                    root: 'gap-2.5',
                    name: 'text-base',
                    description: 'text-sm'
                  },
                  '2xl': {
                    root: 'gap-3',
                    name: 'text-base',
                    description: 'text-base'
                  },
                  '3xl': {
                    root: 'gap-3',
                    name: 'text-lg',
                    description: 'text-base'
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

[TreeA tree view component to display and interact with hierarchical data
structures.](/components/tree)

